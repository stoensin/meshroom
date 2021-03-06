import QtQuick 2.9
import MaterialIcons 2.2
import Controls 1.0

/**
 * DialogsFactory is utility object to instantiate generic purpose Dialogs.
 */
QtObject {

    readonly property string defaultErrorText: "An unexpected error has occured"

    property Component infoDialog: Component {
        MessageDialog {
            title: "Info"
            icon.text: MaterialIcons.info
            visible: true
        }
    }
    property Component warningDialog: Component {
        MessageDialog {
            title: "Warning"
            icon {
                text: MaterialIcons.warning
                color: "#FF9800"
            }
            visible: true
        }
    }
    property Component errorDialog: Component {
        id: errorDialog
        MessageDialog {
            title: "Error"
            icon {
                text: MaterialIcons.error
                color: "#F44336"
            }
            text: defaultErrorText
            visible: true
        }
    }

    function info(window) {
        return infoDialog.createObject(window)
    }

    function warning(window) {
        return warningDialog.createObject(window)
    }

    function error(window) {
        return errorDialog.createObject(window)
    }
}
