/*
    NAME:          popup.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for managing display of popup dialoges
*/

function Popup()
{
    var popup = new Object();
    popup.mask = document.getElementById("page-mask");
    popup.entryFormPopup = document.getElementById("creat-calc");
    popup.aboutPopup = document.getElementById("about-box");
    popup.geneReportPopup = document.getElementById("gene-repo");
    // display the popup mask
    popup.showMask = function()
    {
        this.mask.style.display = "block";
        $('#page-mask').height($(document).height());
    }

    //hide the popup mask
    popup.hideMask = function()
    {
        this.mask.style.display = "none";
    }
    //show the generate report
    popup.showGeneRepoPopup = function()
    {
        this.showMask();
        this.geneReportPopup.style.display = "block";
        this.positionDialogue(this.geneReportPopup);
    }

    // hide the generate report
    popup.hideGeneRepoPopup = function()
    {
        this.hideMask();
        this.geneReportPopup.style.display = "none";
    }


    //show the creatinine clearance calculator form dialog
    popup.showCeatCalcFormPopup = function()
    {
        this.showMask();
        this.entryFormPopup.style.display = "block";
        this.positionDialogue(this.entryFormPopup);
        //this.entryFormPopup.style.left = (($(document).width() / 2) - (this.entryFormPopup.offsetWidth / 2)) + "px";
    }

    // hide the creatinine clearance calculator form dialog
    popup.hideCeatCalcFormPopup = function()
    {

        this.hideMask();
        this.entryFormPopup.style.display = "none";
        let removeelement0 = document.getElementById('result');
        removeelement0.remove();

        document.getElementById("Age").value = "";
        document.getElementById("Weight").value = "";
        document.getElementById("serum").value = "";

        let maleradio0 = document.getElementById('male');
        maleradio0.checked = false;
        let femaleradio0 = document.getElementById('female');
        femaleradio0.checked = false;

    }

    // show the about popup
    popup.showAboutPopup = function()
    {
        this.showMask();
        this.aboutPopup.style.display = "block";
        this.positionDialogue(this.aboutPopup);
    }

    // hide about popup
    popup.hideAboutPopup = function()
    {
        this.hideMask();
        this.aboutPopup.style.display = "none";
    }

    // position dialogue center screen
    popup.positionDialogue = function(popupBox)
    {
        popupBox.style.left = (($(document).width() / 2) - (popupBox.offsetWidth / 2)) + "px";
    }


    popup.calculate = function() {//=>{


        //Getting required values
        let age = document.getElementById("Age").value;
        let weight = document.getElementById("Weight").value;
        let sex = document.querySelector('input[name="sex"]:checked').value;
        let cr = document.getElementById("serum").value;
        //Using a boolean flag whether the sex is female
        let isFemale = sex === 'f' ? true : false;

        //Processing values through the formula
        let result = popup.processValues(age,weight,isFemale,cr)

        //Inserting result element in the DOM
        let element = document.getElementById("br");
        let newElement = `<p id="result">CrCl : ${result}</p>`
        element.insertAdjacentHTML( 'afterend', newElement )

    }

    popup.processValues = (age,weight,isFemale,cr) => {
        let genderFactor = isFemale ? 0.85 : 1;
        return (140-age)*weight*genderFactor/(72*cr)
    }

     popup.reset = () =>{

     //Resetting values
        document.getElementById("Age").value = "";
        document.getElementById("Weight").value = "";
        document.getElementById("serum").value = "";

     //Resetting the radio button
        let maleradio = document.getElementById('male');
        maleradio.checked = false;
        let femaleradio = document.getElementById('female');
        femaleradio.checked = false;

     //removing the DOM element

        let removeelement = document.getElementById('result');
        removeelement.remove();

        }

        popup.generatereport = function ()
        {
        var element = document.getElementById('content');
        element.style.width = element.offsetWidth;
        element.style.height = element.offsetHeight;

        var opt = {
            margin:       0.2,
            filename:     'Report.pdf',
            image:        { type: 'jpeg', quality: 1 },
            html2canvas:  { scale: 2 },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape',precision: '12' }
          };

        // choose the element and pass it to html2pdf() function and call the save() on it to save as pdf.
        html2pdf().set(opt).from(element).save();
        }


    return popup;
}


