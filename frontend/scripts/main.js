$(document).ready(function() {
    // Handle user type selection
    $("#userType").change(function() {
        let userType = $(this).val();
        let extraFields = $("#extraFields");

        extraFields.empty();
        if (userType === "employer") {
            extraFields.append('<input type="text" id="company_name" placeholder="Company Name" required>');
            extraFields.append('<input type="text" id="website" placeholder="Website (Optional)">');
        } else {
            extraFields.append('<input type="text" id="cv_link" placeholder="CV Link (Optional)">');
        }
    });

    // Handle signup
    $("#signupForm").submit(function(e) {
        e.preventDefault();
        
        let userType = $("#userType").val();
        let url = userType === "employer" ? "http://127.0.0.1:5000/api/auth/signup/employer" : "http://127.0.0.1:5000/api/auth/signup/jobseeker";
        
        let userData = {
            full_name: $("#full_name").val(),
            email: $("#email").val(),
            password: $("#password").val()
        };

        if (userType === "employer") {
            userData.company_name = $("#company_name").val();
            userData.website = $("#website").val();
        } else {
            userData.cv_link = $("#cv_link").val();
        }

        $.ajax({
            url: url,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(userData),
            success: function(response) {
                alert(response.message);
                window.location.href = "login.html";
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });

    // Handle login
    $("#loginForm").submit(function(e) {
        e.preventDefault();
        
        $.ajax({
            url: "http://127.0.0.1:5000/api/auth/login",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                email: $("#email").val(),
                password: $("#password").val()
            }),
            success: function(response) {
                localStorage.setItem("access_token", response.access_token);
                alert("Login successful!");
                window.location.href = "dashboard.html";
                $("#welcome-message").text(`Welcome, ${response.full_name}`);
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });

    // Handle logout
    $("#logout").click(function() {
        $.ajax({
            url: "http://127.0.0.1:5000/api/auth/logout",
            type: "POST",
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("access_token")
            },
            success: function(response) {
                localStorage.removeItem("access_token");
                alert(response.msg);
                window.location.href = "index.html";
            },
            error: function(xhr) {
                alert("Logout failed.");
            }
        });
    });
});



 // Handle Job Posting
 $("#jobForm").submit(function(e) {
    e.preventDefault();

    let jobData = {
        job_title: $("#jobTitle").val(),
        description: $("#jobDescription").val(),
        salary: $("#salary").val(),
        location: $("#location").val(),
        company: $("#company").val(),
        website_link: $("#website_link").val()
    };

    $.ajax({
        url: "http://127.0.0.1:5000/api/job/jobs",
        type: "POST",
        contentType: "application/json",
        headers: { "Authorization": "Bearer " + localStorage.getItem("access_token") },
        data: JSON.stringify(jobData),
        success: function(response) {
            alert("Job posted successfully!");
            $("#jobForm")[0].reset();  // Clear form fields
        },
        error: function(xhr) {
            alert(xhr.responseJSON.error);
        }
    });
});