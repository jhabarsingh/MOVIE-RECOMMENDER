
<template>
  <div>
    <v-parallax
      dark
      src="./Home_page.jpg"
      style="height:100vh;position:fixed;width:100%;top:0px;opacity:1;"
    >
      <v-row
        align="center"
        justify="center"
      >
        <v-col
          class="text-center"
          cols="12"
        >
          <v-card
            color="rgba(0, 0, 0, .5 )"
          >
              <h1 class="display-1 font-weight-thick mb-4"
            style="color:white;font-weight:bolder;font-family:Arial;padding:10px; 0px 5px 0px;"
          >
            MOVIE RECOMMENDER
          </h1>

            <MovieSearch />  
          </v-card>  
        
        </v-col>
      </v-row>

    </v-parallax>
  </div>  
</template>

<script>
import MovieSearch from './MovieSearch.vue';

export default {
    components: {
        MovieSearch,
    }
}
</script>