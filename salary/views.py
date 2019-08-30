from django.shortcuts import render,redirect
from .models import esal,edeta
from django.http import HttpResponse
import math
from random import randint
designation=''

def salary(request):
        Basic=65000
        n=Basic/31
        
        leaves_taken=2
        if  Basic > 100000:
                E_id=randint(1,50000) 
                TA=Basic*0.002
                DA=Basic*0.05
                Hra=Basic*0.40
                Special_allowance=Basic*0.27
                ESI=Basic*0.012
                PF=Basic*0.12
                Pension=Basic*0.015
                Insurence=Basic*0.013
                lop=leaves_taken*n
                Gross=Basic+TA+DA+Hra+Special_allowance
                deduction_amount=PF+Pension+Insurence+ESI+lop
                Net_Sal=Gross-deduction_amount
                Deg="DIG"
             
                #return TA,DA,Hra,Gross,PF,Pension,Insurence,Net_Sal
        elif  (Basic > 50000 and Basic < 100000):
                E_id=randint(1,50000)
                TA=Basic*0.0015
                DA=Basic*0.025
                Hra=Basic*0.40
                Special_allowance=Basic*0.25
                ESI=Basic*0.012
                Gross=Basic+TA+DA+Hra+Special_allowance
                PF=Basic*0.10
                Pension=Basic*0.012
                Insurence=Basic*0.010
                lop=leaves_taken*n
                Deg="DSP"
                
                Net_Sal=Gross-(PF+Pension+Insurence+ESI+lop)
               
               
                #return TA,DA,Hra,Gross,PF,Pension,Insurence,Net_Sal
        elif Basic > 30000 and Basic < 50000:
                E_id=randint(1,50000)
                TA=Basic*0.01
                DA=Basic*0.02
                Hra=Basic*0.40
                Special_allowance=Basic*0.05
                ESI=Basic*0.012
                Gross=Basic+TA+DA+Hra+Special_allowance
                PF=Basic*0.08
                Pension=Basic*0.010
                Insurence=Basic*0.010
                lop=leaves_taken*n
                Net_Sal=Gross-(PF+Pension+Insurence+ESI+lop)
                Deg="CI"
               
                
                #return redirect(Salary,TA,DA,Hra,Gross,PF,Pension,Insurence,Net_Sal)
               
        elif  Basic > 20000 and Basic < 30000:
                E_id=randint(1,50000)
                TA=Basic*0.0005
                DA=Basic*0.001
                Hra=Basic*0.40
                Special_allowance=Basic*0.12
                ESI=Basic*0.012
                Gross=Basic+TA+DA+Hra+Special_allowance
                PF=Basic*0.05
                Pension=Basic*0.005
                Insurence=Basic*0.005
                lop=(leaves_taken*n)
                Net_Sal=Gross-(PF+Pension+Insurence+ESI+lop)
                Deg="SI"
                
                #return redirect(Salary,TA,DA,Hra,Gross,PF,Pension,Insurence,Net_Sal)
                
        else:
                E_id=randint(1,50000)
                TA=DA=Hra=Pension=Special_allowance=Insurence=0
                ESI=Pension=Insurence=0
                PF=Basic*0.001
                
                Gross=Basic+TA+DA+Hra+Special_allowance-PF
                lop=leaves_taken*n
                Net_Sal=Gross-lop
                Deg="conistable"
                #return TA,DA,Hra,Gross,PF,Pension,Insurence,Net_Sal
        total_workingdays=31        
        data=esal(
                E_id=E_id,
                Basic=Basic,
                TA=TA,
                DA=DA,
                HRA=Hra,
                Special_allowance=Special_allowance,
                PF=PF,
                Pension=Pension,
                ESI=ESI,
                Insurence=Insurence,
                Gross_Sal=Gross,
                Net_Sal=Net_Sal,
                designation=Deg,
                leaves_taken=leaves_taken,
                total_workingdays=total_workingdays,
                lop=lop)
        data.save()
        return render(request,'salary.html',{'E_id':data.E_id,'Basic':data.Basic,'TA':data.TA,'DA':data.DA,'HRA':data.HRA,
                                'ESI':data.ESI,'Pension':data.Pension,'Insurence':data.Insurence,'Gross_Sal':data.Gross_Sal,
                                'Net_Sal':data.Net_Sal,'PF':data.PF,'deg':data.designation,'Special_allowance':data.Special_allowance,
                                'lop':data.lop,'total_workingdays':data.total_workingdays,'leaves_taken':data.leaves_taken})

def login(request):
        if request.method=='POST':
                global designation
                E_id=request.POST['e_id']
                desig=request.POST['desg']
                data=esal.objects.get(designation=desig,E_id=E_id)
                if not data:
                        return HttpResponse('faild')

                else:
                        return render(request,'salary.html',{'E_id':data.E_id,'Basic':data.Basic,'TA':data.TA,'DA':data.DA,'HRA':data.HRA,
                                'ESI':data.ESI,'Pension':data.Pension,'Insurence':data.Insurence,'Gross_Sal':data.Gross_Sal,
                                'Net_Sal':data.Net_Sal,'PF':data.PF,'deg':data.designation,'Special_allowance':data.Special_allowance,
                                'lop':data.lop,'total_workingdays':data.total_workingdays,'leaves_taken':data.leaves_taken})
        return render(request,'log.html')





def det(request):
        if request.method=='POST':
                desig=request.POST['desi']
                leave=request.POST['leave']
                basic=request.POST['basic']
                if desig==desig:
                        user=esal.objects.filter(designation=desig)
                        if user:
                                return render(request,'dispaly.html',{'user':user})
                        else :
                                user=esal.objects.filter(leaves_taken=leave)
                                if user:
                                        return render(request,'dispaly.html',{'user':user})
                                else:
                                        user=esal.objects.filter(Basic=basic)
                                        if user:
                                                return render(request,'display.html',{'user':user})
                                        else:
                                                return HttpResponse('no Data')                
                        
        return  render(request,'search.html')                  
                        


def deletepage(request):
        return render(request,'delete.html')

def detid(request):
        if request.method=='POST':
                userid=request.POST["id"]
                esal.objects.filter(E_id=userid).delete()
                return render(request,'delete.html')