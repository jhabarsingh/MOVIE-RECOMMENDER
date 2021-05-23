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
        poster: ""
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

              this.id = e.results[0].id;
              this.poster = "https://image.tmdb.org/t/p/original" + e.results[0].backdrop_path;
              
              console.log(this.poster);

              let detail_url = `https://api.themoviedb.org/3/movie/${+this.id}?api_key=${this.api_key}`
              fetch(detail_url).then(ee => {
                    return ee.json();
                }).then(ee => {
                    console.log(ee);

                })

              let cast_url = `https://api.themoviedb.org/3/movie/${+this.id}/credits?api_key=${this.api_key}`
              fetch(cast_url).then(ee => {
                    return ee.json();
                }).then(ee => {
                    let top_cast = ee.null;

                    if(ee.cast.length>=10){
                       top_cast = [0,1,2,3,4,5,6,7,8,9];
                    }
                    else {
                        top_cast = [0,1,2,3,4];
                    }
                    let casts = [];

                    for(var my_cast in top_cast){
                        let obj = {};
                        obj.id = (ee.cast[my_cast].id)
                        obj.name = (ee.cast[my_cast].name);
                        obj.profession = (ee.cast[my_cast].character);
                        obj.profile = ("https://image.tmdb.org/t/p/original"+ee.cast[my_cast].profile_path);
                        casts.push(obj);
                    }   
                    console.log(casts);
                })
            
            
          })
      }
    },

    created () {
        this.states = data;
    }
  }
</script>