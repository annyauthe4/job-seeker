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

    // Handle user's signup
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

                // Redirect to the appropriate dashboard
                if (userType === "employer") {
                    window.location.href = "https://annyauthe4.github.io/job-seeker/employer_dashboard.html";
		} else {
                    window.location.href = "https://annyauthe4.github.io/job-seeker/job_dashboard.html";
		}
            },
            error: function(xhr) {
	        let errorMessage = xhr.responseJSON ? xhr.responseJSON.error : "Signup failed.";
                alert(errorMessage);
            }
        });
    });

    // Handle user's login
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

		//Extract user's role from the user's access token
                const tokenParts = response.access_token.split('.');
                const payload = JSON.parse(atob(tokenParts[1])); // Decode the payload
            
                const role = payload.sub.role;
                if (role === 'employer') {
                  window.location.href = "employer_dashboard.html";
                } else {
                  window.location.href = "job_dashboard.html";
                }
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });

    // Handle user's logout from dashboard
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
                window.location.href = "/index.html";
            },
            error: function(xhr) {
                alert("Logout failed.");
            }
        });
    });
});



 // Handle Employer's Job Posting
 $("#jobForm").submit(function(e) {
    e.preventDefault();

    // Save job information
    let jobData = {
        job_title: $("#jobTitle").val(),
        description: $("#jobDescription").val(),
        salary: $("#salary").val(),
        location: $("#location").val(),
        company: $("#company").val(),
        website_link: $("#website_link").val()
    };

    // Send Job posting information to the database
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

// Fetch all job listings and show them in Jobseeker's dashboard
$.ajax({
    url: "http://127.0.0.1:5000/api/job/jobs",  // API endpoint to fetch all jobs
    type: "GET",
    success: function (jobs) {
        let jobListings = $("#job-listings");
        jobListings.empty();

        if (jobs.length === 0) {
            jobListings.append("<p>No jobs available at the moment.</p>");
        } else {
            jobs.forEach(job => {
                let jobCard = `
                    <div class="job-card">
                        <h3>${job.job_title}</h3>
                        <p><strong>Company:</strong> ${job.company}</p>
                        <p><strong>Description:</strong> ${job.description}</p>
                        <p><strong>Location:</strong> ${job.location}</p>
                        <p><strong>Salary:</strong> ${job.salary}</p>
                        <a href="${job.website_link}" class="apply-link"><button class="apply-button" data-job-id="${job.id}">Apply</button></a>
                    </div>
                `;
                jobListings.append(jobCard);
            });
        }
    },
    error: function (xhr) {
        alert(xhr.responseJSON.error);
    }
});
