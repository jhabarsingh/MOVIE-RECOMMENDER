let data = {
	"text": "Avatar"
}
fetch('http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/', {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});

