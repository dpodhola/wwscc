/*
 * This software is licensed under the GPLv3 license, included as
 * ./GPLv3-LICENSE.txt in the source distribution.
 *
 * Portions created by Brett Wilson are Copyright 2008 Brett Wilson.
 * All rights reserved.
 */


package org.wwscc.dataentry;

import java.awt.Component;
import java.awt.Dimension;
import java.awt.KeyboardFocusManager;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.BorderFactory;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.KeyStroke;
import javax.swing.SwingUtilities;
import net.miginfocom.swing.MigLayout;
import org.wwscc.components.CurrentDatabaseLabel;
import org.wwscc.components.MyIpLabel;
import org.wwscc.storage.Database;
import org.wwscc.storage.Entrant;
import org.wwscc.storage.Run;
import org.wwscc.util.LastManEventQueue;
import org.wwscc.util.Logging;
import org.wwscc.util.MT;
import org.wwscc.util.MessageListener;
import org.wwscc.util.Messenger;


public class DataEntry extends JFrame implements MessageListener
{
	private static final Logger log = Logger.getLogger(DataEntry.class.getName());

	Menus menus;
	EntryModel dataModel;
	SelectionBar setupBar;
	DriverEntry driverEntry;
	ClassTree  numberTree;
	ResultsPane announcer;
	FindEntry finder;
	EntryTable table;
	JScrollPane tableScroll;
	PreregPanel prereg;

	TimeEntry timeEntry;

	JTabbedPane tabs;

	FakeUser fakeUser;  // for debugging

	class HelpPanel extends JLabel implements MessageListener
	{
		private static final long serialVersionUID = -6376824946457087404L;

		public HelpPanel()
		{
			super("Use Tabbed Panels to add Entrants");
			setHorizontalAlignment(CENTER);
			setFont(getFont().deriveFont(12f));
			Messenger.register(MT.OBJECT_CLICKED, this);
			Messenger.register(MT.OBJECT_DCLICKED, this);
		}

		@Override
		public void event(MT type, Object data) {
			switch (type)
			{
				case OBJECT_CLICKED:
					if (data instanceof Entrant)
						setText("Entrant: Ctrl-X or Delete to remove them, Drag to move them, Swap Entrant to change them");
					else if (data instanceof Run)
						setText("Runs: Ctrl-X or Delete to cut, Ctrl-C to copy, Ctrl-V to paste");
					else
						setText("Ctrl-V to paste a Run");
					break;
				case OBJECT_DCLICKED:
					if (data instanceof Entrant)
						setText("Click Swap Entrant to change the entrant for the given runs");
					break;
			}
		}
	}

	public DataEntry() throws IOException
	{
		super("Data Entry");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		menus = new Menus();
		setJMenuBar(menus);

		dataModel = new EntryModel();
		table = new EntryTable(dataModel);
		setupBar = new SelectionBar();
		numberTree = new ClassTree();
		driverEntry = new DriverEntry();
		announcer = new ResultsPane();
		finder = new FindEntry();
		prereg = new PreregPanel(numberTree);


		tabs = new JTabbedPane();
		tabs.setMinimumSize(new Dimension(250, 400));
		tabs.setPreferredSize(new Dimension(250, 768));
		tabs.addTab("Add By Name", driverEntry);
		tabs.addTab("Preregistered", prereg);
		tabs.addTab(" Announcer Data ", announcer);


		tableScroll = new JScrollPane(table);
		tableScroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
		tableScroll.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);

		timeEntry = new TimeEntry();
		menus.add(timeEntry.getTimerMenu());

		CurrentDatabaseLabel curdb = new CurrentDatabaseLabel();
		HelpPanel help = new HelpPanel();
		MyIpLabel myip = new MyIpLabel();
		curdb.setBorder(BorderFactory.createLoweredBevelBorder());
		help.setBorder(BorderFactory.createLoweredBevelBorder());
		myip.setBorder(BorderFactory.createLoweredBevelBorder());

		JPanel infoBoxes = new JPanel(new MigLayout("fill, ins 0", "[18%]0[64%]0[18%]"));
		infoBoxes.add(curdb, "grow");
		infoBoxes.add(help, "grow, hmin 20");
		infoBoxes.add(myip, "grow");

		JPanel content = new JPanel(new MigLayout("fill, ins 1, gap 2",
				"[grow 0][fill][grow 0]",
				"[grow 0][grow 0][]"));
		content.add(setupBar, "spanx 3, growx, wrap");
		content.add(tabs, "spany 2, growx 0, growy");
		content.add(finder, "growx, growy 0, hidemode 2");
		content.add(timeEntry, "spany 2, growx 0, growy, wrap");
		content.add(tableScroll, "grow, wrap");
		content.add(infoBoxes, "spanx 3, growx, wrap");

		fakeUser = new FakeUser(table, timeEntry);

		setContentPane(content);
		setSize(1024,768);
		setVisible(true);
		
		log.log(Level.INFO, "Starting Application: {0}", new java.util.Date());
		
		Messenger.register(MT.OBJECT_DCLICKED, this);
		Database.openDefault();
	}


	@Override
	public void event(MT type, Object o)
	{
		switch (type)
		{
			case OBJECT_DCLICKED:
				if (o instanceof Entrant)
					tabs.setSelectedComponent(driverEntry);
				break;
		}
	}

	/**
	 * Main
	 */
	public static void main(String[] args)
	{
		try
		{
			Class.forName("org.wwscc.dataentry.Sounds");
			Logging.logSetup("dataentry");
			
			SwingUtilities.invokeLater(new Runnable() { public void run() {
				try {
					new DataEntry();
					Toolkit.getDefaultToolkit().getSystemEventQueue().push(new LastManEventQueue());
				} catch (Throwable e) {
					log.log(Level.SEVERE, "DataEntry creation failed: " + e, e);
				}
			}});
		}
		catch (Throwable e)
		{
			log.log(Level.SEVERE, "App failure: " + e, e);
		}
	}
}

