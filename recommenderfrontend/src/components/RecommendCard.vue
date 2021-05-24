<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      :src="poster"
      height="200px"
    ></v-img>

    <v-card-title
        style="font-size:12px;"
    >
      {{movie}}
    </v-card-title>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
        @click="changeRecommender"
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

    </v-card-actions>


  </v-card>
</template>

<script>
  export default {
    data: () => ({
      show: false,
      poster: null
    }),

    props: [
        'movie'
    ],
    methods: {
        getPosters(movie_name) {
            let url = `https://api.themoviedb.org/3/search/movie?api_key=${this.$store.state.api_token}&query=${movie_name}`;
            fetch(url).then(movies => {
                return movies.json();
            }).then(movies => {
                let n = movies.results.length;
                if(n == 0) {
                    // Logic to handle not found;
                }
                
                let movie = movies.results[0];
                
                let poster = "https://image.tmdb.org/t/p/original" + movie.backdrop_path;
                this.poster = (poster)
            })
        },

        changeRecommender() {
            this.$store.state.cast = null;
            localStorage.setItem("movie", this.movie);
            this.$store.state.movie = this.movie;
            console.log(this.$store.state.movie);

            this.$router.replace({ name: 'Recommender', query: { name: this.movie }});
            window.scrollTo(0,0);
        }
    },

    created() {
        this.getPosters(this.movie);
    }
  }
</script>