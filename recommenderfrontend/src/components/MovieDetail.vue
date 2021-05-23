<template>
    <div>
        <MoviePoster/>
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