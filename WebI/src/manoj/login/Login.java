package manoj.login;


import com.crystaldecisions.sdk.exception.SDKException;
import com.crystaldecisions.sdk.framework.CrystalEnterprise;
import com.crystaldecisions.sdk.framework.IEnterpriseSession;
import com.crystaldecisions.sdk.framework.ISessionMgr;
import com.crystaldecisions.sdk.occa.infostore.IInfoStore;


public class Login {
	private ISessionMgr sessionMgr;
	private IEnterpriseSession boSession;
	private IInfoStore istore;
	public boolean debug=false;
	public Login(String username,String password,String cms,String authtype){
		try {
			this.sessionMgr=CrystalEnterprise.getSessionMgr();//get the Session Manager
			this.boSession=sessionMgr.logon(username,password,cms,authtype);//get the Session
			this.istore=(IInfoStore) boSession.getService("InfoStore");//get the Info Store for querying
			
		}
		 catch (SDKException e) {
			 System.err.println("Unable to login or get session");
			if (debug){
				System.out.println("Fail in Constructor Login while logging in");
			}
			e.printStackTrace();
		}
		System.out.println("Logged in to ::: "+boSession.getCMSName());
		
	}
	
	
	/*
	 * Getter Methods for use outside this class if required
	 * 
	 * START
	 */
	
	public void logoffSession(){
		System.out.println("Logging out...");
		this.boSession.logoff();
		System.out.println("Logged out Successfully");
	}
	public IEnterpriseSession getSession(){
		return this.boSession;
	}
	
	public IInfoStore getIstore(){
		return this.istore;
	}
	
	public ISessionMgr getSessionManager(){
		return this.sessionMgr;
	}
	
	//Getter Methods END
}
