<template>
    <div>
        <div v-if="$store.state.casts != null && $store.state.recommended != null">
            <MovieDetail />
      
            
            <v-divider />
            
            <Recommend />

            <Footer />
        </div >
        <div v-else>
            <Loading />
        </div>
    </div>
</template>

<script>
import Loading from './Loading.vue'
import Recommend from './Recommend.vue'
import MovieDetail from './MovieDetail.vue'
import Footer from './Footer.vue'

export default({
    components: {
        Loading,
        Recommend,
        Footer,
        MovieDetail
    },
    data() {
        return {
            api_key: "88797a394acfd740740c5fefa973fca6",
            select: null,
        }
    },
    methods: {
      sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
      },

      fetchDetail() {
          this.select = localStorage.getItem("movie");

          let url = `https://api.themoviedb.org/3/search/movie?api_key=${this.api_key}&query=${this.select}`;
          
          fetch(url).then(movies => {
              return movies.json();
          }).then(movies => {
              let n = movies.results.length;
              if(n == 0) {
                  // Logic to handle not found;
              }
              
              this.$store.state.id = movies.results[0].id;
              this.getMovieDetail(this.$store.state.id);

              this.$store.state.poster = "https://image.tmdb.org/t/p/original" + movies.results[0].backdrop_path;
              
              this.getMovieCast(this.$store.state.id);
          })
      },

      async getMovieDetail(id) {
            let detail_url = `https://api.themoviedb.org/3/movie/${id}?api_key=${this.api_key}`
            
            await fetch(detail_url).then(data => {
                return data.json();
            }).then(data => {
                this.$store.state.movieDetail = data;
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

      async getMovieCast(id) {
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
                let dp = [];
                for(let i in casts) {
                    let temp = (this.getPersonDetail(casts[i].id));
                    dp.push(temp);
                }
    
                this.$store.state.casts = dp;
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
      },

      async getPersonDetail(cast_id) {
          let url = `https://api.themoviedb.org/3/person/${cast_id}?api_key=${this.api_key}&language=en-US`
          
          let data = null;
          await fetch(url).then(details => {
              return details.json();
          }).then(details => {
              data = (details);
          })

          return data;
      },

      movieRecommender () {
          let url = "http://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/"
          
          if(localStorage.getItem("link"))
            url = "https://ec2-3-142-140-94.us-east-2.compute.amazonaws.com:8000/recommender/"

          let movie = {
              "text": localStorage.getItem("movie")
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
              let movies = new Set();
              for(let i=0;  i < this.$store.state.recommended.movies.length; i++) {
                movies.add(this.$store.state.recommended.movies[i]);
              }
              let mob = [];

              movies.forEach(e => {
                mob.push(e);
              })
              console.log(mob);
              this.$store.state.recommended = mob;
            //   this.$store.state.recommended = [];
          })
      }

    },

    created() {
        if(localStorage.getItem("movie")) {
            // Let The page Load
            this.movieRecommender()
            this.sleep(200).then(() => {
                this.fetchDetail();
                console.log(this.$store.state);     
            })
        }
        else {
            this.$router.push("/");
        }
    }

})
</script>
