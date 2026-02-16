# Kubernetes Deployment for IBM i AST Parser

## Files Overview

- `namespace.yaml` - Creates the as400parser namespace
- `configmap.yaml` - Environment configuration
- `secret.yaml` - SMTP credentials (update with your values)
- `deployment.yaml` - Main application deployment
- `service.yaml` - LoadBalancer service for external access
- `ingress.yaml` - GKE Ingress for SSL and domain routing
- `horizontalpodautoscaler.yaml` - Auto-scaling configuration

## Deployment Steps

### 1. Update Configuration

Edit `secret.yaml` and replace the base64 values with your actual SMTP credentials:

```bash
echo -n 'your-smtp-username' | base64
echo -n 'your-smtp-password' | base64
echo -n 'your-smtp-host' | base64
```

Update `deployment.yaml` with your GCP project ID:
```yaml
image: gcr.io/your-project-id/as400parser:latest
```

### 2. Build and Push Docker Image

```bash
# Build the image
docker build -t as400parser:latest .

# Tag for GCR
docker tag as400parser:latest gcr.io/your-project-id/as400parser:latest

# Push to GCR
docker push gcr.io/your-project-id/as400parser:latest
```

### 3. Deploy to GKE

```bash
# Apply all configurations
kubectl apply -f k8s/

# Check deployment status
kubectl get pods -n as400parser
kubectl get services -n as400parser
kubectl get ingress -n as400parser
```

### 4. Verify Deployment

```bash
# Check pod logs
kubectl logs -f deployment/as400parser -n as400parser

# Test the service
kubectl port-forward service/as400parser-service 8080:80 -n as400parser
curl http://localhost:8080/health
```

## Monitoring

```bash
# Check HPA status
kubectl get hpa -n as400parser

# View resource usage
kubectl top pods -n as400parser

# Scale manually if needed
kubectl scale deployment as400parser --replicas=5 -n as400parser
```

## Cleanup

```bash
# Remove all resources
kubectl delete -f k8s/
```
