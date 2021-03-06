package com.example.coronawatch.ui.diagno

import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

import com.example.coronawatch.R

class DiagnoFragment : Fragment() {

    companion object {
        fun newInstance() = DiagnoFragment()
    }

    private lateinit var viewModel: DiagnoViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.diagno_fragment, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        viewModel = ViewModelProviders.of(this).get(DiagnoViewModel::class.java)
        // TODO: Use the ViewModel
    }

}
