/**
 * Created by liu on 2017/6/19/019.
 */
     function firm(operateint ,table,ID) {
    //利用对话框返回的值 （true 或者 false）
    var operate, tablename
    var url
    switch (operateint) {
        case 1:
            operate = 'Add';
            break;
        case 2:
            operate = 'Edit';
            break;
        case 3:
            operate = 'Delete';
            break
    }
    switch (table) {
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
            tablename = 'FamilyPageAdd'
            break
    }
    url=window.location.href
    alert(window.location.href)
    if (operateint==3) {
        if (confirm("你确定提交吗？")) {
             location.href=tablename+operate+'/'+ID
        }
    }
    else {
        location.href=tablename+operate+'/'+ID
    }




}