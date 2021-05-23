<template>
  <v-card
    class="mx-auto"
    max-width="90vw"
    style="margin:50px; 0px;"
  >
    <v-toolbar
      color="indigo"
      dark
    >
      <v-toolbar-title>Movie Cast</v-toolbar-title>

      <v-spacer></v-spacer>

     </v-toolbar>

    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="(card, index) in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.profile"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.name"></v-card-title>
            </v-img>

            <v-card-actions>
              <v-spacer></v-spacer>


              <v-btn icon
                @click="setDialog(index)"
              >
                <v-icon>mdi-send</v-icon>
              </v-btn>

            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <DialogCastDetail />
  </v-card>
</template>


<script>
  import DialogCastDetail from './DialogCastDetail.vue';

  export default {
    data: () => ({
      cards: [

      ],
    }),
    components: {
        DialogCastDetail
    },
    methods: {
        setDialog(key) {
            this.$store.state.present_cast = key;
            this.$store.state.dialog = true;
            console.log(key);
        }
    },

    async created() {
        let item = []
        for(let i in this.$store.state.casts) {
            await this.$store.state.casts[i].then(e => {
                item.push(e);
            })
        }
        for(let i in item) {
            let obj = [];
            obj.name = item[i].name;
            obj.bio = item[i].biography;
            obj.dob = item[i].birthday;
            obj.profession = item[i].known_for_department
            obj.profile = "https://image.tmdb.org/t/p/original" + item[i].profile_path;
            obj.flex = 6;
            this.cards.push(obj);
        }
    }
  }
</script>