<template>
  <div class="text-center">
    <v-dialog
      v-model="$store.state.dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Click Me
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          {{ $store.state.casts[+$store.state.present_cast].name  }}
        </v-card-title>

        <v-img
         height="250"
         :src="url"
        ></v-img>

        <center>
            <v-btn
            class="mx-1"
            color="primary"
            rounded
            style="text-align:center;margin:auto;margin:10px;"
            >
            {{ $store.state.casts[+$store.state.present_cast].known_for_department  }}
            </v-btn>
        </center>
        
        <v-card-text
            style="text-align:justify;"
        >
            {{ $store.state.casts[+$store.state.present_cast].biography }}
         </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="$store.state.dialog = false"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    data () {
      return {
          url: null
      }
    },

    methods: {
        getImage() {
           
        }
    },
    updated() {
         this.url = "https://image.tmdb.org/t/p/original" +  this.$store.state.casts[+this.$store.state.present_cast].profile_path;
     
    }
  }

</script>