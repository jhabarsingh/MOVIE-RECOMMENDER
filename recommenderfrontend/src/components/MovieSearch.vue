<template>
  <v-toolbar
    dark
    color="secondary lighten-1"
    style="margin-bottom:10px;"
  >
    <v-toolbar-title>Movie Name</v-toolbar-title>
    <v-autocomplete
      v-model="select"
      :loading="loading"
      :items="items"
      :search-input.sync="search"
      cache-items
      placeholder="Avatar"
      class="mx-4"
      flat
      hide-no-data
      hide-details
      label="What's your favourite movie?"
      solo-inverted
    ></v-autocomplete>
        <v-btn
            class="ma-2"
            color="secondary"
            dark
            @click="fetchDetail"
            >
            Search
            <v-icon
                dark
                right
            >
                mdi-send
            </v-icon>
        </v-btn>
  </v-toolbar>
</template>

<script>
  import data from './data.js'

  export default {
    data () {
      return {
        loading: false,
        items: [],
        search: null,
        select: "Avatar",
        states: null,
        api_key: "88797a394acfd740740c5fefa973fca6",
        id: null,
        poster: "",
        movie: null,
        casts: null
      }
    },
    watch: {
      search (val) {
        val && val !== this.select && this.querySelections(val)
      },
    },
    methods: {
      querySelections (v) {
        this.loading = true
        // Simulated ajax query
        setTimeout(() => {
          this.items = this.states.filter(e => {
            return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
          })
          this.loading = false
        }, 500)
      },

      fetchDetail() {
          
          let url = `https://api.themoviedb.org/3/search/movie?api_key=${this.api_key}&query=${this.select}`;
          
          fetch(url).then(e => {
              return e.json();
          }).then(e => {
              let n = e.results.length;
              if(n == 0) {
                  // Logic to handle not found;
              }
              console.log(e.results);
              this.movie = e.results[0];
              this.id = e.results[0].id;
              this.getMovieDetail(this.id);

              this.poster = "https://image.tmdb.org/t/p/original" + e.results[0].backdrop_path;
              
              this.getMovieCast(this.id);
          })
      },

      getMovieDetail(id) {
            let detail_url = `https://api.themoviedb.org/3/movie/${id}?api_key=${this.api_key}`
            
            fetch(detail_url).then(data => {
                return data.json();
            }).then(data => {
                console.log(data);
            })

      },

      async getPosters(movie_name) {
        let url = `https://api.themoviedb.org/3/search/movie?api_key=${this.api_key}&query=${movie_name}`;
        let posters = null;
        await fetch(url).then(movies => {
            return movies.json();
        }).then(movies => {
            let n = movies.results.length;
            if(n == 0) {
                // Logic to handle not found;
            }
            
            let movie = movies.results[0];
            
            let poster = "https://image.tmdb.org/t/p/original" + movie.backdrop_path;
            posters = (poster)
        })

        return posters
      },

      getMovieCast(id) {
          let cast_url = `https://api.themoviedb.org/3/movie/${+id}/credits?api_key=${this.api_key}`
            fetch(cast_url).then(movie => {
                return movie.json();
            }).then(movie => {
                let top_cast = null;

                if(movie.cast.length>=10){
                    top_cast = [0,1,2,3,4,5,6,7,8,9];
                }
                else {
                    top_cast = [0,1,2,3,4];
                }
                let casts = [];

                for(var my_cast in top_cast){
                    let obj = {};
                    obj.id = (movie.cast[my_cast].id)
                    obj.name = (movie.cast[my_cast].name);
                    obj.profession = (movie.cast[my_cast].character);
                    obj.profile = ("https://image.tmdb.org/t/p/original"+movie.cast[my_cast].profile_path);
                    casts.push(obj);
                }   
                console.log(casts);
            })
      },
    
      async getMovieIdFromName(movie_name) {
          let url = `https://api.themoviedb.org/3/search/movie?api_key=${this.api_key}&query=${movie_name}`;
          let ids = null;
          await fetch(url).then(movies => {
              return movies.json();
          }).then(movies => {
              let n = movies.results.length;
              if(n == 0) {
                  // Logic to handle not found;
              }
              
              let movie = movies.results[0];
              let id = movie.id;
              ids = id;
         })

         return ids;
      }

    },

    created () {
        this.states = data;
    }
  }
</script>