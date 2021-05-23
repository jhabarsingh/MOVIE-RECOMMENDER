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
            @click="goToRecommender"
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
      }
    },
    watch: {
      search (val) {
        val && val !== this.select && this.querySelections(val)
      },
    },
    methods: {
        goToRecommender () {
            localStorage.setItem("movie", this.select);
            this.$router.push('/recommender')
        }
    },

    created () {
        this.states = data;
    }
  }
</script>