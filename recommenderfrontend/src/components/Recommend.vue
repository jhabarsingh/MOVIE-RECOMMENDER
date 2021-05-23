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
          let url = ""
      }
    },

    created() {
        if(localStorage.getItem("movie_name")) {
            // Let The page Load
        }
        else {
            this.$router.push("/");
        }
    }
    
}
</script>