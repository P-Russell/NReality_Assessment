<template>
  <div class="container">
    <div class="row justify-content-center center-vertical">
      <div class="col col-12 col-lg-8">
        <div class="text-center">
          <h1>Welcome to GitHubber</h1>
          <p class="lead text-muted">
            Enter a users GitHub handle and see their GitHub homepage feed. It's
            Awesome!
          </p>
        </div>
        <div>
          <form
            :class="submitted ? 'was-validated' : 'needs-validation'"
            @submit.prevent="go"
            novalidate
          >
            <div class="form-row justify-content-center">
              <div class="form-group col-6">
                <input
                  type="text"
                  v-model.trim="handle"
                  class="form-control"
                  required
                />
                <div class="invalid-feedback">
                  Please provide a GitHub handle.
                </div>
              </div>
              <div>
                <button class="btn btn-primary px-4">Go!</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      handle: '',
      submitted: false,
    }
  },
  methods: {
    go() {
      this.submitted = true
      if (this.handle) {
        this.$router.push(this.handle + '/current')
      }
    },
  },
}
</script>

<style scoped>
.center-vertical {
  margin-top: 30vh;
}
</style>
