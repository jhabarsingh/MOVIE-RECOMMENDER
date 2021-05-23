<template>
  <div class="text-center"
    style="height:100vh;width:100vw;display:flex;justify-content:center; align-items:center;"
  >

    <v-progress-circular
      :size="150"
      :width="20"
      color="purple"
      indeterminate
    ></v-progress-circular>

  </div>
</template>

<script>
export default {
    name: 'Loading'
}
</script>


<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>