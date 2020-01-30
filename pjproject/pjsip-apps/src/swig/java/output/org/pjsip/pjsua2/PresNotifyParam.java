/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.pjsip.pjsua2;

public class PresNotifyParam {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected PresNotifyParam(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(PresNotifyParam obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  @SuppressWarnings("deprecation")
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        pjsua2JNI.delete_PresNotifyParam(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void setSrvPres(SWIGTYPE_p_void value) {
    pjsua2JNI.PresNotifyParam_srvPres_set(swigCPtr, this, SWIGTYPE_p_void.getCPtr(value));
  }

  public SWIGTYPE_p_void getSrvPres() {
    long cPtr = pjsua2JNI.PresNotifyParam_srvPres_get(swigCPtr, this);
    return (cPtr == 0) ? null : new SWIGTYPE_p_void(cPtr, false);
  }

  public void setState(pjsip_evsub_state value) {
    pjsua2JNI.PresNotifyParam_state_set(swigCPtr, this, value.swigValue());
  }

  public pjsip_evsub_state getState() {
    return pjsip_evsub_state.swigToEnum(pjsua2JNI.PresNotifyParam_state_get(swigCPtr, this));
  }

  public void setStateStr(String value) {
    pjsua2JNI.PresNotifyParam_stateStr_set(swigCPtr, this, value);
  }

  public String getStateStr() {
    return pjsua2JNI.PresNotifyParam_stateStr_get(swigCPtr, this);
  }

  public void setReason(String value) {
    pjsua2JNI.PresNotifyParam_reason_set(swigCPtr, this, value);
  }

  public String getReason() {
    return pjsua2JNI.PresNotifyParam_reason_get(swigCPtr, this);
  }

  public void setWithBody(boolean value) {
    pjsua2JNI.PresNotifyParam_withBody_set(swigCPtr, this, value);
  }

  public boolean getWithBody() {
    return pjsua2JNI.PresNotifyParam_withBody_get(swigCPtr, this);
  }

  public void setTxOption(SipTxOption value) {
    pjsua2JNI.PresNotifyParam_txOption_set(swigCPtr, this, SipTxOption.getCPtr(value), value);
  }

  public SipTxOption getTxOption() {
    long cPtr = pjsua2JNI.PresNotifyParam_txOption_get(swigCPtr, this);
    return (cPtr == 0) ? null : new SipTxOption(cPtr, false);
  }

  public PresNotifyParam() {
    this(pjsua2JNI.new_PresNotifyParam(), true);
  }

}
