let instanceId = null;

document.getElementById('submitBtn').addEventListener('click', async () => {
    const jobDescription = document.getElementById('jobDescription').value;
    console.log('Job Description:', jobDescription);

    try {
        const response = await fetch('http://127.0.0.1:8000/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ context: jobDescription })
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Response:', data);

            // Populate the tag and skills fields with the response data
            document.getElementById('tag').value = data.new_tag;
            document.getElementById('skills').value = data.new_skills;
            instanceId = data.instance_id;
        } else {
            console.error('Error:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

document.getElementById('resumeBtn').addEventListener('click', async () => {
    const tag = document.getElementById('tag').value;
    const skills = document.getElementById('skills').value;

    if (!tag || !skills) {
        alert('Generated Tag and Generated Skills need to be populated first.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/modify_resume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ new_tag: tag, new_skills: skills, instance_id: instanceId })
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Response:', data);
            alert('Resume generated successfully!');
        } else {
            console.error('Error:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
