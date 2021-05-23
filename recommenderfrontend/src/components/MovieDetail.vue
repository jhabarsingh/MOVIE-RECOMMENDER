<template>
    <div>
        <MoviePoster />
        
        <!-- <v-card-title class="text-center justify-center py-6">
            <h1 class="font-weight-bold display-3 basil--text">
            MOVIE CAST
            </h1>
        </v-card-title> -->
        
        <MovieCastDetail />
    </div>
</template>


<script>
import MovieCastDetail from './MovieCastDetail.vue'
import MoviePoster from './MoviePoster.vue'

export default {
    data() {
        return ({
            
        })
    },
    components: {
        MovieCastDetail,
        MoviePoster
    },
    props: [
        'movies'
    ],

    methods: {
    },

    created() {
        if(localStorage.getItem("movie")) {
            // Let The page Load
        }
        else {
            this.$router.push("/");
        }
    }
    
}
</script>