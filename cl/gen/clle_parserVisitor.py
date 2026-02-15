# Generated from C:/Users/natar/AI/AS400Parser/grammars/clle_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .clle_parser import clle_parser
else:
    from clle_parser import clle_parser

# This class defines a complete generic visitor for a parse tree produced by clle_parser.

class clle_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by clle_parser#program.
    def visitProgram(self, ctx:clle_parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#statement.
    def visitStatement(self, ctx:clle_parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:clle_parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#typeValue.
    def visitTypeValue(self, ctx:clle_parser.TypeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#lenValue.
    def visitLenValue(self, ctx:clle_parser.LenValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#assignment.
    def visitAssignment(self, ctx:clle_parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#loop.
    def visitLoop(self, ctx:clle_parser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#conditional.
    def visitConditional(self, ctx:clle_parser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#label.
    def visitLabel(self, ctx:clle_parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#pgmStatement.
    def visitPgmStatement(self, ctx:clle_parser.PgmStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#command.
    def visitCommand(self, ctx:clle_parser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#commandParam.
    def visitCommandParam(self, ctx:clle_parser.CommandParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#paramValue.
    def visitParamValue(self, ctx:clle_parser.ParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#condition.
    def visitCondition(self, ctx:clle_parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#expression.
    def visitExpression(self, ctx:clle_parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#dataType.
    def visitDataType(self, ctx:clle_parser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#startValue.
    def visitStartValue(self, ctx:clle_parser.StartValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#endValue.
    def visitEndValue(self, ctx:clle_parser.EndValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by clle_parser#stepValue.
    def visitStepValue(self, ctx:clle_parser.StepValueContext):
        return self.visitChildren(ctx)



del clle_parser