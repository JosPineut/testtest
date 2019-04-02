import xlsxwriter


#TEMPORARY STUFF
workbook = xlsxwriter.Workbook('CommentsPerLanguage.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0


#TEMPORARY STUFF
    worksheet.write(row, col, df_id.get(x))
    try:
        worksheet.write(row, col + 1, df_text.get(x))
        worksheet.write(row, col + 2, str(detect(df_text.get(x))))
    except:
        worksheet.write(row, col + 1, " ")
        worksheet.write(row, col + 2, "nl")
    worksheet.write(row, col + 3,df_sentiment.get(x))
    worksheet.write(row, col + 4, df_training.get(x))
    row += 1

workbook.close()