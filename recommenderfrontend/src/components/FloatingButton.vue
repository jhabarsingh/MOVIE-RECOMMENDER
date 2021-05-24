<template>
    <v-fab-transition>
        <v-btn
        v-show="!hidden"
        color="pink"
        dark
        fixed
        bottom
        right
        fab
        @click="dhandhanadhan"
        >
        <v-icon>mdi-home</v-icon>
        </v-btn>
    </v-fab-transition>
</template>

<script>
export default {
    methods: {
        dhandhanadhan() {
            localStorage.removeItem("goBack");
            this.$router.push("/");
        }
    }
}
</script>