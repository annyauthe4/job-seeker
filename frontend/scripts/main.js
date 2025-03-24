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
        let url = userType === "employer" ? "/api/signup/employer" : "/api/signup/jobseeker";
        
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
            url: "/api/login",
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
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });

    // Handle logout
    $("#logout").click(function() {
        $.ajax({
            url: "/api/logout",
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
