require(['knockout',
    'ojs/ojarraydataprovider',
    'ojs/ojvalidation-base',
    'ojs/ojknockout',
    'ojs/ojtable',
    'ojs/ojvalidation-datetime',
    'ojs/ojvalidation-number'
], function (ko, ArrayDataProvider, ValidationBase) {
    'use strict';

    let ViewModel = function () {

        // for salary fields
        const salOptions = {
            style: 'currency',
            currency: 'USD'
        };
        const salaryConverter = ValidationBase.Validation.converterFactory("number").createConverter(salOptions);

        // for date fields
        const dateOptions = {
            formatStyle: 'date',
            dateFormat: 'medium'
        };
        const dateConverter = ValidationBase.Validation.converterFactory("datetime").createConverter(dateOptions);

        // the use of arrow functions works just fine
        this.formatSal = data => salaryConverter.format(data);
        this.formatDate = data => dateConverter.format(data);

        var employeesArray = JSON.parse(JSON.parse(document.getElementById('employees').textContent));
        var empsArray = [];
        employeesArray.forEach(function (employee) {
            var emp = {empno: employee.pk,
                       fname: employee.fields.first_name,
                       lname: employee.fields.last_name,
                       email: employee.fields.email,
                       phone: employee.fields.phone_number,
                       job: employee.fields.job_id,
                       hiredate: employee.fields.hire_date,
                       sal: employee.fields.salary,
                       comm: employee.fields.commission_pct,
                       manager: employee.fields.manager_id,
                       dept: employee.fields.department_id};

            empsArray.push(emp);
        });

        this.dataProvider = new ArrayDataProvider(empsArray, {
            keyAttributes: "empno"
        });
    };
    ko.applyBindings(new ViewModel(), document.getElementById('table'));
});