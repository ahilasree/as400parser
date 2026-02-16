"""
Web API endpoint for IBM i AST Parser UI
Provides REST API to run parser and get results
"""

import os
import sys
import json
import tempfile
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

# Add project root to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import run_pipeline, InputSpec, ExportOptions

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/parse', methods=['POST'])
def parse_files():
    """Parse IBM i files and return results"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'files' not in data:
            return jsonify({'error': 'Missing files in request'}), 400
        
        files = data['files']
        mode = data.get('mode', 'combined')
        enable_pdf = data.get('enable_pdf', False)
        enable_email = data.get('enable_email', False)
        email_config = data.get('email_config', {})
        
        # Create temporary files for processing
        temp_dir = tempfile.mkdtemp()
        temp_files = []
        
        try:
            # Copy files to temp directory
            for file_path in files:
                if os.path.exists(file_path):
                    temp_file = os.path.join(temp_dir, os.path.basename(file_path))
                    with open(file_path, 'r', encoding='utf-8') as src:
                        with open(temp_file, 'w', encoding='utf-8') as dst:
                            dst.write(src.read())
                    temp_files.append(temp_file)
            
            # Build export options
            export_options = None
            if enable_pdf:
                pdf_path = os.path.join(temp_dir, 'report.pdf')
                export_options = ExportOptions(
                    enable_pdf=True,
                    pdf_path=pdf_path,
                    enable_email=enable_email,
                    email_to=email_config.get('to') if enable_email else None,
                    email_subject="IBM i Analysis Report",
                    email_smtp_config={
                        "host": email_config.get('smtp_host'),
                        "port": int(email_config.get('smtp_port', 587)),
                        "username": email_config.get('smtp_user'),
                        "password": email_config.get('smtp_pass'),
                        "use_tls": email_config.get('smtp_tls', 'true').lower() == 'true'
                    } if enable_email else None
                )
            
            # Create input specs
            inputs = []
            for temp_file in temp_files:
                inputs.append(InputSpec(path=temp_file, type='file'))
            
            # Run pipeline
            result = run_pipeline(inputs, mode=mode, export=export_options)
            
            # Prepare response
            response_data = {
                'success': True,
                'diagnostics_count': len(result.diagnostics),
                'cl_results': len(result.cl_results),
                'rpg_results': len(result.rpg_results),
                'db2_results': len(result.db2_results),
                'dspf_results': len(result.dspf_results),
                'analysis_reports': []
            }
            
            # Add analysis reports
            for cl_result in result.cl_results:
                response_data['analysis_reports'].append({
                    'file': cl_result.path,
                    'type': 'CL',
                    'report': cl_result.summary_report,
                    'ast_tree': cl_result.ast_tree
                })
            
            for rpg_result in result.rpg_results:
                response_data['analysis_reports'].append({
                    'file': rpg_result.path,
                    'type': 'RPG', 
                    'report': rpg_result.summary_report,
                    'ast_tree': rpg_result.ast_tree
                })
            
            for db2_result in result.db2_results:
                response_data['analysis_reports'].append({
                    'file': db2_result.path,
                    'type': 'DB2',
                    'report': db2_result.summary_report,
                    'ast_tree': db2_result.ast_tree
                })
            
            for dspf_result in result.dspf_results:
                response_data['analysis_reports'].append({
                    'file': dspf_result.path,
                    'type': 'DSPF',
                    'report': dspf_result.summary_report,
                    'ast_tree': dspf_result.ast_tree
                })
            
            # Add PDF file if generated
            if enable_pdf and os.path.exists(pdf_path):
                response_data['pdf_file'] = pdf_path
            
            return jsonify(response_data)
            
        finally:
            # Cleanup temp files
            import shutil
            if 'temp_dir' in locals():
                shutil.rmtree(temp_dir, ignore_errors=True)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/parse', methods=['GET'])
def parse_info():
    """Get parsing API information"""
    return jsonify({
        'title': 'IBM i AST Parser API',
        'version': '1.0.0',
        'endpoints': {
            'parse': {
                'method': 'POST',
                'description': 'Parse IBM i files (CL, RPG, DB2, DSPF)',
                'parameters': {
                    'files': ['array of file paths'],
                    'mode': ['combined|cl|rpg|db2|dspf'] ,
                    'enable_pdf': ['boolean'],
                    'enable_email': ['boolean'],
                    'email_config': {
                        'to': ['email address'],
                        'smtp_host': ['SMTP host'],
                        'smtp_port': ['port number'],
                        'smtp_user': ['SMTP username'],
                        'smtp_pass': ['SMTP password'],
                        'smtp_tls': ['true|false']
                    }
                }
            }
        }
    })

@app.route('/api/parse', methods=['OPTIONS'])
def handle_options():
    """Handle CORS preflight requests"""
    return '', 204

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'IBM i AST Parser API'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run in development mode
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    # Run in production mode
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
