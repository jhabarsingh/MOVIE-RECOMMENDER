<template>
    <div>
        Movie Cast List
    </div>
</template>


<script>

export default {
    data() {
        return ({
            
        })
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