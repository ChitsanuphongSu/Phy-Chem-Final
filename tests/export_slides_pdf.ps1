$ErrorActionPreference = 'Stop'
$out = 'D:\Luna\Phy-Chem\physical-chemistry-study-hub\outputs\slides'
$powerPoint = New-Object -ComObject PowerPoint.Application
try {
    foreach ($name in @('01_Complete_Revision','02_Exam_Focus','03_Formula_and_Problems')) {
        $pptx = Join-Path $out "$name.pptx"
        $pdf = Join-Path $out "$name.pdf"
        $deck = $powerPoint.Presentations.Open($pptx, $true, $false, $false)
        try { $deck.SaveAs($pdf, 32) } finally { $deck.Close() }
    }
} finally {
    $powerPoint.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
}
