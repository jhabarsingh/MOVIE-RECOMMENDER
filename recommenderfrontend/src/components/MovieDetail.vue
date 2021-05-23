<template>
    <div>
        Movie Detail
        <MovieCastDetail />
    </div>
</template>


<script>
import MovieCastDetail from './MovieCastDetail.vue'

export default {
    data() {
        return ({
            
        })
    },
    components: {
        MovieCastDetail
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