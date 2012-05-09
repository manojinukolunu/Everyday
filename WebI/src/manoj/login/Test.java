package manoj.login;


import java.util.Iterator;

import com.crystaldecisions.sdk.exception.SDKException;
import com.crystaldecisions.sdk.occa.infostore.IInfoObject;
import com.crystaldecisions.sdk.occa.infostore.IInfoObjects;
import com.crystaldecisions.sdk.occa.infostore.IInfoStore;

public class Test {
	public enum SIKIND{
		AuditAdmin,CacheServerAdmin,Calendar,Category,CMSAdmin,Connection,CrystalReport,Diskunmanaged,
		Event,EventServerAdmin,Excel,FavoritesFolder,Folder,FileServerAdmin,Ftp,FullClient,
		Hyperlink,Inbox,JobServerAdmin,LicenseKey,Managed,ObjectPackage,Overload,PageServerAdmin,
		PersonalCategory,Pdf,Powerpoint,Profile,Program,Publication,ReportAppServerAdmin,
		Rtf,Server,Shortcut,Smtp,SSOAdmin,Txt,Universe,User,Usergroup,Webi,WebiServerAdmin,
		Word,NOVALUE;
		
		public static SIKIND toInt(String str){
			try{
				return valueOf(str);
			}
			catch(Exception e){
				return NOVALUE;
			}
		}
	}
	
	@SuppressWarnings("unchecked")
	public static void main(String args[]) throws SDKException{
		Login login=new Login("Administrator","password01","yadra05-tm1","secEnterprise");
		//
		IInfoStore istore=login.getIstore();
		String query="select SI_NAME from CI_INFOOBJECTS";
		IInfoObjects objects=istore.query(query);
		Iterator<Object> it=objects.iterator();
		int [] arr=new int[44];
		while(it.hasNext()){
			//System.out.println(SIKIND.values().length);
			IInfoObject object=(IInfoObject) it.next();
			switch (SIKIND.toInt(object.getKind())){
			case AuditAdmin:
			    arr[0]++;
			    break;
			    
			case CacheServerAdmin:
			    arr[1]++;
			    break;
			    
			case Calendar:
			    arr[2]++;
			    break;
			    
			case Category:
			    arr[3]++;
			    break;
			    
			case CMSAdmin:
			    arr[4]++;
			    break;
			    
			case Connection:
			    arr[5]++;
			    break;
			    
			case CrystalReport:
			    arr[6]++;
			    break;
			    
			case Diskunmanaged:
			    arr[7]++;
			    break;
			    
			case Event:
			    arr[8]++;
			    break;
			    
			case EventServerAdmin:
			    arr[9]++;
			    break;
			    
			case Excel:
			    arr[10]++;
			    break;
			    
			case FavoritesFolder:
			    arr[11]++;
			    break;
			    
			case Folder:
			    arr[12]++;
			    break;
			    
			case FileServerAdmin:
			    arr[13]++;
			    break;
			    
			case Ftp:
			    arr[14]++;
			    break;
			    
			case Hyperlink:
			    arr[15]++;
			    break;
			    
			case Inbox:
			    arr[16]++;
			    break;
			    
			case JobServerAdmin:
			    arr[17]++;
			    break;
			    
			case LicenseKey:
			    arr[18]++;
			    break;
			    
			case Managed:
			    arr[19]++;
			    break;
			    
			case ObjectPackage:
			    arr[20]++;
			    break;
			    
			case Overload:
			    arr[21]++;
			    break;
			    
			case PersonalCategory:
			    arr[22]++;
			    break;
			    
			case Pdf:
			    arr[23]++;
			    break;
			    
			case Powerpoint:
			    arr[24]++;
			    break;
			    
			case Profile:
			    arr[25]++;
			    break;
			    
			case Program:
			    arr[26]++;
			    break;
			    
			case Publication:
			    arr[27]++;
			    break;
			    
			case Rtf:
			    arr[28]++;
			    break;
			    
			case Server:
			    arr[29]++;
			    break;
			    
			case Shortcut:
			    arr[30]++;
			    break;
			    
			case Smtp:
			    arr[31]++;
			    break;
			    
			case SSOAdmin:
			    arr[32]++;
			    break;
			    
			case Txt:
			    arr[33]++;
			    break;
			    
			case Universe:
			    arr[34]++;
			    break;
			    
			case User:
			    arr[35]++;
			    break;
			    
			case Usergroup:
			    arr[36]++;
			    break;
			    
			case Webi:
			    arr[37]++;
			    break;
			    
			case Word:
			    arr[38]++;
			    break;
			    
			case NOVALUE:
			    arr[39]++;
			    break;
			    
			}
			
		}
		
		login.logoffSession();
		System.out.println(
				" \nAuditAdmin= " +arr[0]+
				" \nCacheServerAdmin= " +arr[1]+
				" \nCalendar= " +arr[2]+
				" \nCategory= " +arr[3]+
				" \nCMSAdmin= " +arr[4]+
				" \nConnection= " +arr[5]+
				" \nCrystalReport= " +arr[6]+
				" \nDiskunmanaged= " +arr[7]+
				" \nEvent= " +arr[8]+
				" \nEventServerAdmin= " +arr[9]+
				" \nExcel= " +arr[10]+
				" \nFavoritesFolder= " +arr[11]+
				" \nFolder= " +arr[12]+
				" \nFileServerAdmin= " +arr[13]+
				" \nFtp= " +arr[14]+
				" \nHyperlink= " +arr[15]+
				" \nInbox= " +arr[16]+
				" \nJobServerAdmin= " +arr[17]+
				" \nLicenseKey= " +arr[18]+
				" \nManaged= " +arr[19]+
				" \nObjectPackage= " +arr[20]+
				" \nOverload= " +arr[21]+
				" \nPersonalCategory= " +arr[22]+
				" \nPdf= " +arr[23]+
				" \nPowerpoint= " +arr[24]+
				" \nProfile= " +arr[25]+
				" \nProgram= " +arr[26]+
				" \nPublication= " +arr[27]+
				" \nRtf= " +arr[28]+
				" \nServer= " +arr[29]+
				" \nShortcut= " +arr[30]+
				" \nSmtp= " +arr[31]+
				" \nSSOAdmin= " +arr[32]+
				" \nTxt= " +arr[33]+
				" \nUniverse= " +arr[34]+
				" \nUser= " +arr[35]+
				" \nUsergroup= " +arr[36]+
				" \nWebi= " +arr[37]+
				" \nWord= " +arr[38]+
				" \nNOVALUE= " +arr[39]
				);
		
	}

}
