/**
 * Created by liu on 2017/6/19/019.
 */
     function firm(operateint ,table,ID) {
    //利用对话框返回的值 （true 或者 false）
    var operate, tablename
    var url
    switch (operateint) {
        case 0:
            operate='';
            break;
        case 1:
            operate = 'Add';
            break;
        case 2:
            operate = 'Edit';
            break;
        case 3:
            operate = 'Delete';
            break;
    }
    switch (table) {
        case 0:
            tablename='Form';
            break;
        case 1:
            tablename = 'EmpPage';
            break;
        case 2:
            tablename = 'EducationPage';
            break;
        case 3:
            tablename = 'CoursePage';
            break;
        case 4:
            tablename = 'JobPage';
            break;
        case 5:
            tablename = 'FamilyPage'
            break;
    }
    // url=window.location.href
    // re=/^.+\/information/
    // urlbase=re.exec(url)
    urlbase='http://'+window.location.host+'/information'
     // alert(urlbase+'/'+tablename+operate+'/'+ID)
    // alert(window.location.host)
    // alert(url)
    if (operateint==3) {
        if (confirm("你确定提交吗？")) {
             location.href=urlbase+'/'+tablename+operate+'/'+ID
        }
    }
    else {
        location.href=urlbase+'/'+tablename+operate+'/'+ID
    }




}