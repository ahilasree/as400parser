/* Enhanced RPG Example with Comprehensive Business Rules */
     H DFTACTGRP(*YES)
     
/* Data Definitions */
     D OrderNum        S             10
     D CustNum        S             10
     D Amount         S             9  2
     D TaxAmount      S             9  2
     D TotalAmount    S             9  2
     D ValidOrder     S               N
     D ErrorMsg       S             50
     D CustomerName   S             30
     
/* File Definitions */
     FORDERHDR    IF   E           K DISK
     F                                    RENAME(ORDERHDR:ORDHDR)
     F                                    USRINP
     F                                    USROPN
     F                                    PREFIX(ORDHDR)
     
     FCUSTMAST    IF   E           K DISK
     F                                    RENAME(CUSTMAST:CUST)
     F                                    USRINP
     F                                    USROPN
     F                                    PREFIX(CUST)
     
/* Main Program Logic */
     C     *Entry        PLIST
     C                   PARM           OrderNum
     C                   PARM           ErrorMsg
     
/* Field Validation Rules */
     C                   CHAIN     OrderNum    ORDHDR                90
     C                   IF        *IN90
     C                   EVAL      ErrorMsg = 'Order not found'
     C                   RETURN
     C                   ENDIF
     
     C                   CHAIN     CustNum     CUST                 91
     C                   IF        *IN91
     C                   EVAL      ErrorMsg = 'Customer not found'
     C                   RETURN
     C                   ENDIF
     
/* Business Calculation Rules */
     C                   EVAL      TaxAmount = Amount * 0.07
     C                   EVAL      TotalAmount = Amount + TaxAmount
     
/* Data Validation Rules */
     C                   IF        Amount < 0
     C                   EVAL      ErrorMsg = 'Amount cannot be negative'
     C                   RETURN
     C                   ENDIF
     
     C                   IF        TotalAmount > 99999.99
     C                   EVAL      ErrorMsg = 'Total amount exceeds limit'
     C                   RETURN
     C                   ENDIF
     
/* File Operations Rules */
     C                   UPDATE    ORDHDR
     C                   IF        *IN90
     C                   EVAL      ErrorMsg = 'Update failed'
     C                   RETURN
     C                   ENDIF
     
/* Indicator Logic Rules */
     C                   SETON                                     90
     C                   IF        *IN90
     C                   EVAL      ValidOrder = *ON
     C                   ENDIF
     
/* Procedure Call Rules */
     C                   CALLP     SendConfirmation(OrderNum:CustomerName)
     C                   IF        ErrorMsg <> *BLANKS
     C                   RETURN
     C                   ENDIF
     
/* Data Transformation Rules */
     C                   MOVE      CustomerName    CustomerName
     C                   MOVEL     CustomerName    FormattedName
     C                   CAT       'Order: '       OrderNum     OrderDesc
     
     C                   SETON                                     LR
     C                   RETURN
