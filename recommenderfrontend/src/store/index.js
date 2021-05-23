import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    api_token: "88797a394acfd740740c5fefa973fca6",
    movie: null,
    id: null,
    poster: null,
    movieDetail: null,
    casts: null,
    recommended: null,
    dialog: false,
    present_cast: false

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
