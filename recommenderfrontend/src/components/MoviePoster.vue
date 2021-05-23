<template>
  <v-row justify="center">
    <v-img
      :src="$store.state.poster"
      lazy-src="./Home_page.jpg"
      width="100vw"
      height="100vh"
      
    >
      <template v-slot:placeholder>
        <v-row
          class="fill-height ma-0"
          align="center"
          justify="center"
        >
          <v-progress-circular
            indeterminate
            color="grey lighten-5"
          ></v-progress-circular>
        </v-row>
      </template>
    </v-img>
  </v-row>
</template>

<script>
export default {
}
</script>