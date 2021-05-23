<template>
  <div>
    <v-container class="grey lighten-5"
      v-if="$store.state.recommended.length != 0"
    >

     <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold display-3 basil--text">
        RECOMMENDATIONS
      </h1>
    </v-card-title>
      <v-row no-gutters>
        <v-col
          v-for="n in $store.state.recommended"
          :key="n"
          cols="12"
          sm="6"
          style="padding:5px;"
        >
            <RecommendCard :movie="n" />
        </v-col>
      </v-row>
    </v-container>
    
    <div v-else>
      <no-data />
    </div>
    
  </div>
</template>

<script>
import RecommendCard from './RecommendCard.vue'
import NoData from './NoData.vue'
export default {
    components: {
        RecommendCard,
        NoData
    },
    data: () => ({
        
    }),
    methods: {

    }
}
</script>


<style>
/* Helper classes */
.basil {
  background-color: #FFFBE6 !important;
}
.basil--text {
  color: #356859 !important;
}
</style>