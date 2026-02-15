# Generated from C:/Users/natar/AI/AS400Parser/grammars/db2_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .db2_parser import db2_parser
else:
    from db2_parser import db2_parser

# This class defines a complete generic visitor for a parse tree produced by db2_parser.

class db2_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by db2_parser#sqlScript.
    def visitSqlScript(self, ctx:db2_parser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#sqlStatement.
    def visitSqlStatement(self, ctx:db2_parser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#semicolon.
    def visitSemicolon(self, ctx:db2_parser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#selectStatement.
    def visitSelectStatement(self, ctx:db2_parser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#selectList.
    def visitSelectList(self, ctx:db2_parser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#selectItem.
    def visitSelectItem(self, ctx:db2_parser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#alias.
    def visitAlias(self, ctx:db2_parser.AliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#tableExpression.
    def visitTableExpression(self, ctx:db2_parser.TableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#tableReference.
    def visitTableReference(self, ctx:db2_parser.TableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#tableFunctionName.
    def visitTableFunctionName(self, ctx:db2_parser.TableFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#viewName.
    def visitViewName(self, ctx:db2_parser.ViewNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#indexName.
    def visitIndexName(self, ctx:db2_parser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#sequenceName.
    def visitSequenceName(self, ctx:db2_parser.SequenceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#joinClause.
    def visitJoinClause(self, ctx:db2_parser.JoinClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#joinCondition.
    def visitJoinCondition(self, ctx:db2_parser.JoinConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#columnList.
    def visitColumnList(self, ctx:db2_parser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#whereClause.
    def visitWhereClause(self, ctx:db2_parser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#groupByClause.
    def visitGroupByClause(self, ctx:db2_parser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#havingClause.
    def visitHavingClause(self, ctx:db2_parser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#orderByClause.
    def visitOrderByClause(self, ctx:db2_parser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#orderByItem.
    def visitOrderByItem(self, ctx:db2_parser.OrderByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#limitClause.
    def visitLimitClause(self, ctx:db2_parser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#offsetClause.
    def visitOffsetClause(self, ctx:db2_parser.OffsetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#fetchClause.
    def visitFetchClause(self, ctx:db2_parser.FetchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#insertStatement.
    def visitInsertStatement(self, ctx:db2_parser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#valueList.
    def visitValueList(self, ctx:db2_parser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#arguments.
    def visitArguments(self, ctx:db2_parser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#updateStatement.
    def visitUpdateStatement(self, ctx:db2_parser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#setClause.
    def visitSetClause(self, ctx:db2_parser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#deleteStatement.
    def visitDeleteStatement(self, ctx:db2_parser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#mergeStatement.
    def visitMergeStatement(self, ctx:db2_parser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#mergeCondition.
    def visitMergeCondition(self, ctx:db2_parser.MergeConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#updateClause.
    def visitUpdateClause(self, ctx:db2_parser.UpdateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#insertClause.
    def visitInsertClause(self, ctx:db2_parser.InsertClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#createStatement.
    def visitCreateStatement(self, ctx:db2_parser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#createTableStatement.
    def visitCreateTableStatement(self, ctx:db2_parser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#columnDefinition.
    def visitColumnDefinition(self, ctx:db2_parser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#dataType.
    def visitDataType(self, ctx:db2_parser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#precision.
    def visitPrecision(self, ctx:db2_parser.PrecisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#scale.
    def visitScale(self, ctx:db2_parser.ScaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#length.
    def visitLength(self, ctx:db2_parser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#columnConstraint.
    def visitColumnConstraint(self, ctx:db2_parser.ColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#defaultValue.
    def visitDefaultValue(self, ctx:db2_parser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#checkCondition.
    def visitCheckCondition(self, ctx:db2_parser.CheckConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#createViewStatement.
    def visitCreateViewStatement(self, ctx:db2_parser.CreateViewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#createIndexStatement.
    def visitCreateIndexStatement(self, ctx:db2_parser.CreateIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#createSequenceStatement.
    def visitCreateSequenceStatement(self, ctx:db2_parser.CreateSequenceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#startValue.
    def visitStartValue(self, ctx:db2_parser.StartValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#incrementValue.
    def visitIncrementValue(self, ctx:db2_parser.IncrementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#minValue.
    def visitMinValue(self, ctx:db2_parser.MinValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#maxValue.
    def visitMaxValue(self, ctx:db2_parser.MaxValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#alterStatement.
    def visitAlterStatement(self, ctx:db2_parser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#alterAction.
    def visitAlterAction(self, ctx:db2_parser.AlterActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#constraintName.
    def visitConstraintName(self, ctx:db2_parser.ConstraintNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#constraintDefinition.
    def visitConstraintDefinition(self, ctx:db2_parser.ConstraintDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#dropStatement.
    def visitDropStatement(self, ctx:db2_parser.DropStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#objectName.
    def visitObjectName(self, ctx:db2_parser.ObjectNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#grantStatement.
    def visitGrantStatement(self, ctx:db2_parser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#privilegeList.
    def visitPrivilegeList(self, ctx:db2_parser.PrivilegeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#privilege.
    def visitPrivilege(self, ctx:db2_parser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#objectType.
    def visitObjectType(self, ctx:db2_parser.ObjectTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#granteeList.
    def visitGranteeList(self, ctx:db2_parser.GranteeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#grantee.
    def visitGrantee(self, ctx:db2_parser.GranteeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#revokeStatement.
    def visitRevokeStatement(self, ctx:db2_parser.RevokeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#commitStatement.
    def visitCommitStatement(self, ctx:db2_parser.CommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#rollbackStatement.
    def visitRollbackStatement(self, ctx:db2_parser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#beginStatement.
    def visitBeginStatement(self, ctx:db2_parser.BeginStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#savepointName.
    def visitSavepointName(self, ctx:db2_parser.SavepointNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#setStatement.
    def visitSetStatement(self, ctx:db2_parser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#optionName.
    def visitOptionName(self, ctx:db2_parser.OptionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#optionValue.
    def visitOptionValue(self, ctx:db2_parser.OptionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#commentStatement.
    def visitCommentStatement(self, ctx:db2_parser.CommentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#expression.
    def visitExpression(self, ctx:db2_parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#primaryExpression.
    def visitPrimaryExpression(self, ctx:db2_parser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#literal.
    def visitLiteral(self, ctx:db2_parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#columnReference.
    def visitColumnReference(self, ctx:db2_parser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#tableName.
    def visitTableName(self, ctx:db2_parser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#columnName.
    def visitColumnName(self, ctx:db2_parser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#parameter.
    def visitParameter(self, ctx:db2_parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#operator.
    def visitOperator(self, ctx:db2_parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:db2_parser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#comparisonOperator.
    def visitComparisonOperator(self, ctx:db2_parser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#logicalOperator.
    def visitLogicalOperator(self, ctx:db2_parser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#functionCall.
    def visitFunctionCall(self, ctx:db2_parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#functionName.
    def visitFunctionName(self, ctx:db2_parser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#argumentList.
    def visitArgumentList(self, ctx:db2_parser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#windowFunction.
    def visitWindowFunction(self, ctx:db2_parser.WindowFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#windowFunctionName.
    def visitWindowFunctionName(self, ctx:db2_parser.WindowFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#windowSpecification.
    def visitWindowSpecification(self, ctx:db2_parser.WindowSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#frameSpecification.
    def visitFrameSpecification(self, ctx:db2_parser.FrameSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#frameStart.
    def visitFrameStart(self, ctx:db2_parser.FrameStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#frameEnd.
    def visitFrameEnd(self, ctx:db2_parser.FrameEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#caseExpression.
    def visitCaseExpression(self, ctx:db2_parser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#whenClause.
    def visitWhenClause(self, ctx:db2_parser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#whenExpression.
    def visitWhenExpression(self, ctx:db2_parser.WhenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#thenExpression.
    def visitThenExpression(self, ctx:db2_parser.ThenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#elseExpression.
    def visitElseExpression(self, ctx:db2_parser.ElseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#castExpression.
    def visitCastExpression(self, ctx:db2_parser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by db2_parser#subquery.
    def visitSubquery(self, ctx:db2_parser.SubqueryContext):
        return self.visitChildren(ctx)



del db2_parser