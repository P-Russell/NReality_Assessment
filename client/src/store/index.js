import { API } from '../plugins/api'

const api = new API()

export const state = () => ({
  entries: '__LOADING__',
  filter: null,
  applyFilter: false,
})

export const mutations = {
  setEntries(state, entries) {
    state.entries = entries
  },
  removeEntry(state, entryId) {
    state.entries = state.entries.filter((entry) => entry.id !== entryId)
  },
  setFilter(state, value) {
    state.filter = value
  },
  setApplyFilter(state, value) {
    state.applyFilter = value
  },
}

export const getters = {
  entries: (state) => {
    if (state.applyFilter && state.entries !== '__LOADING__') {
      return state.entries.filter((entry) =>
        entry.content['#text']
          .toLowerCase()
          .includes(state.filter.toLowerCase())
      )
    }
    return state.entries
  },
}

export const actions = {
  async fetchEntries({ commit }, data) {
    commit('setEntries', '__LOADING__')
    const entries = await api.fetchFeed(data.handle, data.readLater)
    commit('setEntries', entries)
  },
  async setReadLater({ commit }, data) {
    await api.addToReadLater(data.handle, data.entryId)
    commit('removeEntry', data.entryId)
  },
}
