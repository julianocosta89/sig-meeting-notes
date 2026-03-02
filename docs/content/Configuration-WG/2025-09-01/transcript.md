SIG: Configuration WG
Date: 2025-09-01
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 00:35 Hello?
I'm not sure I can hear you.
**GZ Gregor Zeitlinger** 01:07 Test… Better?
**Dan Gomez Blanco** 01:09 Yep, I can see the clearing out.
**GZ Gregor Zeitlinger** 01:14 Have you been here 2 weeks ago?
**Dan Gomez Blanco** 01:17 I think I was here, like, no, some time ago.
**GZ Gregor Zeitlinger** 01:22 Oh, okay.
**Dan Gomez Blanco** 01:23 But not two weeks… I don't think I was here 2 weeks ago, yeah.
**GZ Gregor Zeitlinger** 01:29 Oh, we have a US holiday. I forgot about that.
**Dan Gomez Blanco** 01:33 Maybe.
**GZ Gregor Zeitlinger** 01:35 Probably not going to be many today.
**Dan Gomez Blanco** 01:40 Oh, is it a U.S. holiday today, alright.
**GZ Gregor Zeitlinger** 01:42 Yeah, I just opened the meeting agenda, and it… Sit there.
**Dan Gomez Blanco** 01:48 I just, I mean, I'm not actively that actively involved in…
in this SIG, but I join whenever I can as a part of a governance committee to be…
To see, you know, see what's happening.
**GZ Gregor Zeitlinger** 02:02 You're a GC, okay.
**Dan Gomez Blanco** 02:04 Yeah, yeah, and just, you know.
be of any help that I can be, in case,
There's any… anything that… that you need help with.
**GZ Gregor Zeitlinger** 02:14 Yeah, Traska's, heavily involved in the project, and he's also GC, so…
**Dan Gomez Blanco** 02:20 Yeah.
**GZ Gregor Zeitlinger** 02:21 We're not missing out.
**Dan Gomez Blanco** 02:23 I think… I think, yeah, Trask asked me to… to pick up on that, because I think he's got, now, a clash, and he's not able to make these meetings, I believe.
**GZ Gregor Zeitlinger** 02:32 Semantic conventions is at the same time right.
**Dan Gomez Blanco** 02:35 Yeah, yeah, that's the… that's the… that's the one. So he asked me to join this one.
**GZ Gregor Zeitlinger** 02:40 Yeah. Good point.
Yeah, I guess, we won't have much attendance today.
Do you have anything?
**Dan Gomez Blanco** 02:54 Not really, just wanted to say, I guess…
Thanks to… Alex, that updated the… The project's timelines,
I can go through that if you want. So we've been trying to… this is part of the…
part of the governance… sorry, part of the graduation process, we're getting some of the…
Process… processes that we've got reviewed.
And.
Sorry, I just don't know what I put in there. And, one of them is related to roadmap. How do we manage the roadmap? How do we communicate what's happening in OpenTelemetry? And it's something that we've been working on for a long time, and then now we've got this, OpenTelemetry roadmap.
That is… let me just pull a… put a link in there, bye.
I can find it.
Yeah.
Put it in the chat.
So that project now is a…
a consolidated view of things that are happening in OpenTelemetry. They don't need to be all projects.
These can be initiatives that are driven by a specific SIG, that's already…
you know, working on something. The only requirement is that they are… Listed in the community… sex.yaml.
So… Pointing to that as well.
**GZ Gregor Zeitlinger** 04:37 Okay, and now I can see declarative configuration is…
Planned to be stable spring next year.
**Dan Gomez Blanco** 04:45 Yeah, so Alex added that the target dates, so if you go… if you go to the…
If you click on the…
What is it?
declarative is the number 2, right, in that list. So if you click on it, you should be able to see an issue, that it's only… it's only an issue that's holding, or that it's being synced from the underlying
Projects, which is the project board.
And then if you click on the project.
and you go to the declarative Config Stability Board.
And there is a thing at the top right that says, on track.
And that was updated 2 weeks ago by Alex.
And it has some target dates.
Some start date for the project.
Which started in 2022.
And target date is 2026. I think it's a conservative date, and we can only be,
It's open source at the end of the day.
So, but, yeah, it's, it's…
**GZ Gregor Zeitlinger** 05:53 I don't think it's conservative at all.
of the project.
**Dan Gomez Blanco** 05:57 I know, yeah, so that's what, that's what Alex said, is like, let's play… I know that they wanted to get, like, the first of, like…
M… Yeah.
That done, basically, potentially… M…
sooner, but I think that's a good date. And then it can always be adjusted, right? That's the thing that we're trying to… we're trying to achieve. What we're trying to achieve with this is not, like…
Not to have a date to, you know, beat people with, but more like we're communicating the current best
like, estimate that we've got, right? So if we need to pull it… push it back, we push it back.
If we can bring it forward, we bring it forward. But it's a way for the community to get a little bit of a…
Of a clearer view on what's happening in the hotel.
And this helps a lot, too.
Thanks to everyone here that was able to get a clear… I mean, even just having the project board, that helps a lot, right?
So…
**GZ Gregor Zeitlinger** 06:56 Yep, I was just working on some, on, like, a sub-part of this today, which is,
stability milestones for Java, which is what I'm working on.
**Dan Gomez Blanco** 07:07 Cool.
**GZ Gregor Zeitlinger** 07:09 I'll just put it in the doc here,
I want to check it out,
So, I started with a single project, and now I've broken it into different milestones, because,
Project keeps, getting bigger and bigger the more, I… poke at it.
**Dan Gomez Blanco** 07:30 Yeah.
Cool.
So that's got my… yeah, that's… that's… That's great.
**GZ Gregor Zeitlinger** 07:39 If you want to know more about it, we have a dedicated meeting for Declarative Config Java, which is on Thursdays.
But Traska's there, so.
**Dan Gomez Blanco** 07:48 Is that part of a Java SIG, or is that being driven…
**GZ Gregor Zeitlinger** 07:52 Yes.
**Dan Gomez Blanco** 07:53 Cool.
Yeah, so I think that's, that's… I spoke to Trask about this as well, and I think, you know, the new… this new way of,
So, if you go back to the…
Should I go and share my screen? That'll make it easier.
**GZ Gregor Zeitlinger** 08:13 Sure.
**Dan Gomez Blanco** 08:15 So this new way, I mean, you can see here on the left that…
Either one is, like, a one-to-one.
Because this is only taken from the projects that are in the, sort of, like, community projects, right? Things that are happening across…
Most of these are, like, cross… Sig?
Projects, but they're, you know, led by someone, but, like, at the end of the day, they're, like.
You know, they're like, a lot of enzymatic conventions, but the idea here, with this roadmap.
Is that they don't all need to be… need to have a project dog, and approval from the governance committee, and the technical committee, and, like, all that.
project management process that we've got in place for, like, bigger things. But, if there is something that, for example, like, the JavaSig is working on.
you know, stability for the Cloud Config, and that is… Something that's being solely…
driven by the… well, like, yeah, driven by the JavaSig.
then you should be able to just add, like, the board that you showed there, the projects for JavaSig… for Java…
or config stability in Java.
That could be added here, right? And then we've got…
**GZ Gregor Zeitlinger** 09:30 Do you want to edit right now, or…
**Dan Gomez Blanco** 09:32 We've got a little bit of, so, it is actually in… Community Roadmap.
So here… There is a document that explains how things are added there. Which is basically…
In the 6.yaml. So we've got this roadmap sync.
Thing.
So the only thing that one needs to do is to add it here to the sector.yaml, so if there's a…
Yeah, so each SIG now has a list of roadmap project IDs.
So if you wanted to add that to the JavaSig, you just need to add this property to the sig.yaml with the ID of the project.
And then the rest will… start to… to work.
**GZ Gregor Zeitlinger** 10:26 Add this link to the document, and then we can discuss it next time, because
I think, just adding Java doesn't make sense. We could add the projects for all the other languages as well.
**Dan Gomez Blanco** 10:38 Yeah, okay, that makes sense, yeah. And then, because those will be driven by the specific… SIGs, right? So…
**GZ Gregor Zeitlinger** 10:45 Yep, that's right.
**Dan Gomez Blanco** 10:47 Cool. I like the… I like that. I'll add that in a second.
Mmm…
But yeah, that should be as easy as, like, adding the ID there, and then it should count towards, like, the things that each SIG are working on.
**GZ Gregor Zeitlinger** 11:00 Yeah, okay, cool.
Can you add it to the…
**Dan Gomez Blanco** 11:03 The document? Yeah, okay,
What is it? If I can find it.
Cool Just add it there.
Cool. Okay.
That should explain it.
I'm more in detail.
**GZ Gregor Zeitlinger** 12:12 Huh?
**Dan Gomez Blanco** 12:19 Okay.
I've got nothing else, so…
**GZ Gregor Zeitlinger** 12:26 Me neither, because most of the things are in Java now, and I have decided to put all the
cross-seq-related issues into the milestone 2 and 3, because otherwise I'll never make any progress. Alright, have a great day!
**Dan Gomez Blanco** 12:45 Right, you too. Bye-bye.
