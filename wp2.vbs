Option Explicit

Dim strURL, strSavePath

' URL of the Bing wallpaper image
strURL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

' Save path for the downloaded image
strSavePath = "C:\Users\XXXX\wallpaper\1.jpg"

Dim objHTTP, objStream, objFSO, objFile
Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP")
Set objStream = CreateObject("ADODB.Stream")
Set objFSO = CreateObject("Scripting.FileSystemObject")

objHTTP.Open "GET", strURL, False
objHTTP.Send

If objHTTP.Status = 200 Then
    Dim responseJson, imageUrl
    responseJson = objHTTP.responseText
    
    ' Parse the JSON response to extract the image URL
    imageUrl = Mid(responseJson, InStr(responseJson, """url"":""") + 8)
    imageUrl = Left(imageUrl, InStr(imageUrl, """") - 1)
    
    ' Construct the complete image URL
    imageUrl = "https://www.bing.com/" & imageUrl
    
    ' Save the imageUrl to a text file
    Dim txtFilePath
    txtFilePath = "C:\Users\680242\wallpaper\test.txt"
    
    Set objFile = objFSO.CreateTextFile(txtFilePath, True)
    objFile.WriteLine imageUrl
    objFile.Close
    
    ' Download the image file
    objHTTP.Open "GET", imageUrl, False
    objHTTP.Send

    If objHTTP.Status = 200 Then
        objStream.Open
        objStream.Type = 1
        objStream.Write objHTTP.ResponseBody
        objStream.SaveToFile strSavePath, 2 ' 1 = no overwrite, 2 = overwrite
        objStream.Close
    Else
        MsgBox "Error downloading the image: " & objHTTP.Status, vbExclamation
    End If
Else
    MsgBox "Error retrieving Bing API response: " & objHTTP.Status, vbExclamation
End If

Set objStream = Nothing
Set objHTTP = Nothing
Set objFSO = Nothing
