/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.pjsip.pjsua2;

public class TxMsgEvent {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected TxMsgEvent(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(TxMsgEvent obj) {
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
        pjsua2JNI.delete_TxMsgEvent(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void setTdata(SipTxData value) {
    pjsua2JNI.TxMsgEvent_tdata_set(swigCPtr, this, SipTxData.getCPtr(value), value);
  }

  public SipTxData getTdata() {
    long cPtr = pjsua2JNI.TxMsgEvent_tdata_get(swigCPtr, this);
    return (cPtr == 0) ? null : new SipTxData(cPtr, false);
  }

  public TxMsgEvent() {
    this(pjsua2JNI.new_TxMsgEvent(), true);
  }

}
