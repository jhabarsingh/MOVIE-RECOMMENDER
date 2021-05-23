<template>
    
</template>


<script>

export default {
    data() {
        return ({
            
        })
    },
    
    methods: {
      async movieRecommender () {
          let url = "http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/"
          let movie = {
              "text": this.$store.state.movie
          }
          let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(movie),
          }

          fetch(url, options).then(e => {
              return e.json();
          }).then(details => {
              this.$store.state.recommended = details;
          })
      }
    },

    created() {
        if(localStorage.getItem("movie")) {
            // Let The page Load
        }
        else {
            this.$router.push("/");
        }
    }
    
}
</script>