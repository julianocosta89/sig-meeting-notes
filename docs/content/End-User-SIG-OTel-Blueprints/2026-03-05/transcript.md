SIG: End-User SIG: OTel Blueprints
Date: 2026-03-05
Duration: 94 minutes
Zoom Recording URL: https://zoom.us/rec/share/z6cWmEnIEv9gnuSiEZprBCCox7yeM6lTja2Xi3vaDfl6cVSu7i_s3G4vuDnYqHOa.axAmKqHX5Rnjvbco
============================================================

## Zoom Recording Transcript

Joy 00:18:39 I enjoy you.
Yes, I'm… Good to wait on.
Nope.
Excuse me.
Beautiful.
-Oh.
Alright.
Wang Zhu.
neil yashinsky 01:05:28 Hello, everyone.
Tiffany Hrabusa 01:05:34 female.
neil yashinsky 01:05:38 Hi, Tiffany, how are you today? Hello, Joy.
Tiffany Hrabusa 01:05:45 I'm good, thanks. How are you? And, hi, Joy.
Joy 01:05:49 Yeah, hi, everyone.
Nice to see you again.
Tiffany Hrabusa 01:05:58 I'm eating lunch, so I'm going to keep my camera off for a little while.
neil yashinsky 01:06:04 Yeah, same. But, to answer your question, Tiffany, very good, thank you.
Dan Gomez Blanco 01:06:29 Hello?
Tiffany Hrabusa 01:06:36 Hello.
Dan Gomez Blanco 01:07:58 Just wait another couple minutes for people to join, and then we can get started.
Kyle Shelton 01:09:11 Good morning.
Dan Gomez Blanco 01:09:16 Hi there.
Okay, we can probably… Get started
One second, I will share my screen.
Cool, okay. So, agenda for today, here's the… I'm gonna paste the link.
on… Zoom…
If you want to add topics to the agenda.
Let's start with the first one, then.
Which is between robots, because the meeting has already been recorded. Yes, I will actually have already claimed host of a meeting, and yeah, booted them.
I might try to reach out. I think I know who that bot is… was from, so, just to re… I'll reach out to them.
Yeah, so that they know that. Meetings are recorded at where they are.
Okay, so, next one is from me.
Which is related to the Blueprint template.
There's a PR opened, which I took what I originally did in Google Docs, and then put it here.
there is a document here, there's a sort of, there's a comment from, from Jacob.
yeah, so I think it's a fair comment related to…
Give people some type of, like.
Troubleshooting… perhaps not troubleshooting, but, like… What are some of the…
Yeah, what are some of the things that can go wrong when you operate an architecture of a certain,
of a certain type, and where to… where to start looking, basically. I think that's the idea, to include it in the template.
Which makes sense, so I think we should probably…
Included. I would expect an appendix or something like that to go into detail, there's an appendix section in here.
So I think something like the list of alerts might be going into too much detail for what a blueprint's supposed to be, but it could go into an appendix.
But yeah, I will… I've not really had time.
In the last couple of weeks, due to…
personal circumstances to look at this, but yeah, I will…
Next week, I will work on this and… and… And address that comment.
So, yeah, if you have any comments, please add them there, and I would also appreciate if you have any comments to, say.
Because there were people… there were people here that were,
called out as contributors in the project proposal. We don't have yet a GitHub group for…
for Blueprint approvers, so… If you could just leave a comment in there.
That would probably be just enough for now, saying, like, hey, this looks good, let's just go with it. I don't think it needs to be perfect, either, we can just, you know, as we're writing blueprints, we can just get back to the template and add more if we need to, or remove, okay? So yeah, so if you leave a comment there saying, like, this looks good, then we can just merge this.
At the moment, just to make sure that…
everyone here's on the same page. In OpenTelemetry, there is,
multiple groups, GitHub groups, or GitHub teams, sorry. Each SIG will have, like, a list of approvers, a list of, well, a list of triagers, approvers, and maintainers.
is the same for the SIG end user as well.
However… I will have spoken to the rest of the SIG leadership, and
Yeah, I think we think it's a good idea.
to have… Blueprint approvers in the future.
I think right now, we're still… I guess, you know, the, the, the, the process will probably…
Mature as we go forward.
But yeah, I think it will make sense to have some blueprints approvers, because at the moment, the SIG end user
does have approvers, but they're not specifically… I think the skill set is different for the current people that are in the second user approvers, which are more related to, like, you know, running the OpenTelemetry live sessions, and sharing content, and blog posts, and surveys, and so on.
Compared to perhaps, like, the group that would be of interest, the SIG end user approvers.
So… yeah.
As we mature, and as this project goes and, and, you know, gets things into…
into the website, and Blueprints delivered.
Of course, if anyone that writes blueprints and reviews blueprints would like to be added to this group, to then review blueprints in the future and approve them, I would be very much appreciated. So you can reach out to me whenever you want, and then, you know, we can, we can make sure that
That we, yeah, that we talk about that, how that would work in the future.
But yeah, for now, if you can just leave a comment here, saying that, hey, this looks good, then that would be all that's required.
neil yashinsky 01:15:25 Can I, inquire on that, Dan? So…
For now, then, we're… are you looking for us to first…
provide comments on the Blueprint template itself before we start working on any of the specific blueprints.
Dan Gomez Blanco 01:15:41 Well, I mean… I think, considering that the blueprint
template was already in… in, you know, sort of, like, pre-agreased before we opened this PR.
you can probably already start working on a similar template. I don't think it will change much compared to, you know, we already…
had a sort of agreement that this is generally good, right? It's just more, like, it's a matter of, like.
giving it a… as if it were, like, a PR approval, right? But without…
having the access to approved APR.
Yeah, I guess…
neil yashinsky 01:16:14 Tails for me.
Dan Gomez Blanco 01:16:15 Yeah, exactly. That's just more like, so it's recorded here, that it's just not me.
Without any type of, like, backing from the rest of the group to come up with this, right?
neil yashinsky 01:16:25 I'll just, confess, like, total,
unfamiliarity with the process of updating. Can you scroll back up again? Because I'd love to, you know, contribute on this, and I'm looking at the, you were just looking at the view, maybe it was in 2.30 itself?
Dan Gomez Blanco 01:16:43 Yeah, this one.
neil yashinsky 01:16:45 So, just like, for me and maybe anybody else who has never done this before, like, we're just looking to, like, check out that template.md, make our changes in line, check it back in, is that, including comments, is that right?
Dan Gomez Blanco 01:16:59 No, just the comments, I don't…
neil yashinsky 01:17:01 Oh, I see.
Dan Gomez Blanco 01:17:02 Yeah, just add any comments here, like, you can add.
neil yashinsky 01:17:04 I see.
Dan Gomez Blanco 01:17:05 Yeah. Okay, perfect, yes, thank you.
neil yashinsky 01:17:08 That's how new I am.
Alain Pham 01:17:09 That means, yeah, if we're good, we just hit the top right, submit review, and then just put a comment in there, right?
Dan Gomez Blanco 01:17:16 I don't know if you're not part… if everyone here is part of OpenTelemetry, then you would be able to do this.
I don't know if you're not part of the org?
If you're, like, able to see even this button, but, like…
neil yashinsky 01:17:30 Hmm.
Dan Gomez Blanco 01:17:30 I'm not entirely sure. But even if you're not, then any comment here in the conversation is… you're definitely able to do this, right? So add a comment here.
neil yashinsky 01:17:38 Okay, appreciate that, thanks.
Alain Pham 01:17:41 Got it.
Dan Gomez Blanco 01:17:43 Awesome.
Cool, yep.
So, I think after that, I've gotten the… so, I think had in my backlog as well, the… starting with the blueprints, but yeah, no, please start already with whatever you're, like, working on. Of the back of that one. I don't think it would change much, even if we… if we have comments to address, right?
Cool.
Tiffany.
Tiffany Hrabusa 01:18:12 Hello.
So, we've talked about this a couple times, and there's an outstanding issue.
I think the last time we talked synchronously, we kind of settled on Mermaid, but then the discussion and the issue brought up, D2, which is also an open source
Diagrams as code, tool.
I think it has a little bit more extensibility than Mermaid does, so you can make more complex diagrams.
I checked with, the communications SIG, and
they don't see any problem with it. From what I…
very quickly understood of the workflow with D2. You have, like, a .d2 file that has the configuration for the image in it, which all… which gets checked into the repo, but then you're also generating an SVG from that.
neil yashinsky 01:19:08 Yeah.
Tiffany Hrabusa 01:19:08 And so we wouldn't actually need to…
add any kind of support to the website. As long as there's an SVG, then we can just refer to that in the Markdown files. So, yeah, there's no additional overhead required from Tom's side of things. I guess we just need to decide whether we want to go Mermaid or D2.
And then, I can kind of…
Work up some, like, general style guidelines, depending on which tool we pick.
Just so that the diagrams kind of look the same.
Dan Gomez Blanco 01:19:42 That would be awesome, actually, yeah. The,
the question that I've got is, like, is there a…
I know nothing about D2, right? Is there a visual…
Visual tool that one can use to, To… to draw these, or… And then translate.
Tiffany Hrabusa 01:20:04 I think so.
Dan Gomez Blanco 01:20:05 Code, yeah.
Tiffany Hrabusa 01:20:07 Oh, I don't… I don't think it goes that way, but I think they have…
A mechanism where it, like.
continually render, so as you make changes to the code, you see those changes in real time, but I… I haven't… yeah, exactly.
Dan Gomez Blanco 01:20:21 Alright, okay, so you can, you can play with this and that stuff here, and then… okay, I see.
Tiffany Hrabusa 01:20:27 So, yeah.
Alain Pham 01:20:29 So no… no drag and drop is, it's just pure… Code declaration, right?
Tiffany Hrabusa 01:20:36 I haven't used the playground. Dan just discovered that, so maybe it is possible to start with the visual representation and create the code from there, or the configuration from there. I'm not really sure.
Dan Gomez Blanco 01:20:52 It doesn't… doesn't look like it. I mean, that's one of my things, like, you know, where, like.
I know that someone mentioned, in the issue… I know that I'm just sort of, like, going back to the original discussion, but…
Someone mentioned, even DrawIO, so,
I guess what we're trying to achieve is not that it renders directly in the page, what we're trying to achieve is that one can check out the diagram.
And then, either in the PNG, embedded in the PNG, or, like, or a separate file.
You can then edit it, right, as a download.
Tiffany Hrabusa 01:21:31 Yes.
Yeah, we want them to be easily editable, so that we can keep these blueprints up to date.
I've heard from other comms folks that they also use draw.io in their own work, but I don't…
I think that that would create an additional overhead, and the images might get out of date pretty quickly. So I'm fine sticking with Mermaid if we don't want to add a new tool to the workflow here.
I just… Same. You know, we can just decide, now which one we want to go with, and then I can create some style guidelines from there.
neil yashinsky 01:22:12 I'll just say there was one consideration I thought, that was raised about localization
Which I don't know if it's a concern or not, I just… it was, like, raised, and that's… I think if we have a tool that currently suits all of our existing needs, then it's much easier to stay with that, especially if the people who, you know, are using it, I don't know if there's any, like, existing knowledge base associated with that use, but…
The same is usually always better, unless there's some specific gap we're trying to address.
Tiffany Hrabusa 01:22:41 Agreed. The other advantage of using Mermaid is that the website…
dark mode will work with Mermaid. It turns the diagrams, into dark mode diagrams, whereas an SVG would just appear as the light version that we… that we use.
Dan Gomez Blanco 01:23:00 Do you know of any, parts here that I use in Mermaid, off the top of your head?
Tiffany Hrabusa 01:23:04 Yeah, if you go to the collector architecture page…
Dan Gomez Blanco 01:23:14 Oh, alright, okay.
Right, that's… yeah, that's actually pretty ticketed.
Tiffany Hrabusa 01:23:25 So that is another consideration, whereas the SVGs, or the static images, don't convert when you switch to dark mode.
I think the one plus on the side of D2 is that I think you can probably do more with it than you can with Mermaid.
But…
I don't know… I guess we don't know what we don't know yet, like, how complex these diagrams are going to get, so…
Dan Gomez Blanco 01:23:52 Yeah, so… as we don't know, is it, like, worth then sticking with Mermaid and…
And if we find that we need something else later, maybe, like, that's a discussion we can have later.
As in, we know, we know mermaids, right? I mean, it's being used across…
Other parts of the web, so… I don't think.
Tiffany Hrabusa 01:24:15 Yeah.
Dan Gomez Blanco 01:24:16 I think we have a list of requirements right now, at least I don't have a list of requirements that I know fulfilled by… by Mermaid in these diagrams, but…
Tiffany Hrabusa 01:24:23 Yep, no, that's… Mermaid is… is absolutely fine with me. I was just following up on the issue discussion to make sure.
That that's what we wanted to do.
Dan Gomez Blanco 01:24:32 Yeah.
So… Sorry, I just don't know why I stopped sharing. So Neil, so what's it,
Tom was making a comment on that.
Yeah, Neil, I get your comment. Yeah, it's go with the status quo, and… Okay.
Tiffany Hrabusa 01:24:55 Okay, great. I will.
Dan Gomez Blanco 01:24:56 Yeah, I'll comment on the issue as well. I think I changed… I think I've been convinced of just, keep on using mermaids.
Tiffany Hrabusa 01:25:05 Okay, and I will, create an issue to…
come up with some basic style guidelines. For the most part, we stick to the defaults with Mermaid, because they work the best with dark mode, so there may not even be that many, conventions, necessarily, to… to…
spell out. But I'll take a look at that and make sure that it gets added to the template, either in the current PR or in a follow-up PR.
I think that's it for me.
Dan Gomez Blanco 01:25:54 Sorry, I was on mute. The last thing in the board,
is to… yeah, I just wanted to check if everything here…
is, I guess, up-to-date? There are things that someone is working on that we should move into in progress, or…
Or something else.
lciukaj@splunk.com 01:26:18 I started working on my blueprint, and then that's 245.
Dan Gomez Blanco 01:26:22 Cool, awesome.
lciukaj@splunk.com 01:26:23 non-Kubernetes environments, so this is still in progress, it can still stay where it is.
Dan Gomez Blanco 01:26:28 Have we agreed on the… I guess, yeah, this is the agreed, scope for this, right?
lciukaj@splunk.com 01:26:33 So there is a draft already, a Google Docs link.
hope that everyone can access, so that… if you could review with Daniel, in the free time, give me some feedback if the form is okay.
And also, if anyone else wants to contribute to that, feel free to add some comments or adjust the document.
Kyle Shelton 01:26:56 I'll take a look at that one, sorry.
lciukaj@splunk.com 01:26:59 I was wondering, like, if…
Because there is, like, two concepts, like, one is a blueprint, another is reference architecture. So, should we have some diagrams in a blueprint itself?
Dan Gomez Blanco 01:27:12 I think, yeah.
lciukaj@splunk.com 01:27:14 I think it depends, right? But if there is a need for that, to explain something in, let's say, graphical way, then we can include… So far, I don't have… I don't have any images, but I'm thinking I can include a couple of them in the blueprint.
Dan Gomez Blanco 01:27:29 Yeah, yeah, so I think so. I think I would expect to have diagrams in the blueprint.
And then, you know, like.
I mean, the reference architecture is almost just basically, like, almost like a reference implementation, right? Someone took that blueprint, or, like, parts of the blueprint.
And then implement it in a way that…
That you can back it with.
Like, a specific thing, right? So, that… yeah.
That makes sense.
Okay. Yeah, if someone can have a look at this, I'm gonna be…
So until probably next week, or end of next week, I might not be able to.
To have a look at this, but but yeah, I will.
If anyone else wants to, also.
Give some comments here, then, yeah, that'll be appreciated.
Alain Pham 01:28:23 Yeah, I can have a look at it as well.
Dan Gomez Blanco 01:28:26 Awesome.
Good stuff.
lciukaj@splunk.com 01:28:30 And then, quick question here, should I go ahead and open PR for that, or it's too early? I mean, once we have more content, and let's say, first review in the doc, then we should start with the PR.
Dan Gomez Blanco 01:28:42 I think, let's wait for… I don't know, because we're all quite, I guess, you know, quite new here. I think we're still trying to… as in the process.
I would say that give it a week or so for it to, like, get some comments here, and then we can open the PR.
lciukaj@splunk.com 01:28:59 Sounds good. Ray, thanks.
Dan Gomez Blanco 01:29:09 It was another… Have not been able to… Have a sync with the…
DevX SIG folks to understand the reference architecture part,
As in, I know they've got some already for the collector.
And it's for Collector.
architecture patterns.
But yeah, I'll… I have started the conversation, but I will,
Ensure that we reflect that here in these issues.
So yeah, I'll take that, I'll take that action as well.
Kyle Shelton 01:29:46 Just a note, Dan, Alex is on, maternity leave.
So, he's probably gonna be delayed. If you wanna assign me that Kubernetes, I can work on it while he's out.
Dan Gomez Blanco 01:29:59 Thank you.
There we go.
Yeah, so it'd be good in this one to… if we have already… alright, I see that we have a…
Have you…
Kyle Shelton 01:30:16 He's got a dock already.
Dan Gomez Blanco 01:30:19 Cool.
So the scope of this is understood, right? I mean, I didn't really add it in the… normally this would be…
an issue template, so we would have, like, the scope as… whoever opened the issue would have the scope. But, yeah, let me know if,
I'll have a look through this, and then…
get the scope in the description, so it's easier to… Awesome.
To read.
Okay.
Anything else?
Any other questions?
lciukaj@splunk.com 01:30:52 Nothing from my side. I'm good.
Dan Gomez Blanco 01:30:54 I was gonna ask if anybody is going to be at KubeCon Amsterdam?
Tiffany Hrabusa 01:31:04 Ultimately not.
neil yashinsky 01:31:05 Not at this time, it's planned, at least.
lciukaj@splunk.com 01:31:08 This time.
Unfortunately.
neil yashinsky 01:31:11 Saving episode.
Alain Pham 01:31:12 for me.
lciukaj@splunk.com 01:31:12 My proposals were rejected, so hopefully next time.
Dan Gomez Blanco 01:31:18 Yeah, yeah, I…
as much customer travel, I know. Don't know about it. But yeah, so, yeah, I think, you know, normally there is… although I think this year there is no open telemetry Observatory, but I'll…
I'll see what the newly, like.
forums community managers, newly elected community managers, like Rhys and Adriana, and, and so on. The,
they might have some… I don't know if they're planning…
an open… normally, like, I just… by the way, for those that have not been to GoopCon, there is an OpenTelemetry Observatory booth, where, like.
we normally tend to have sessions, and my idea was to have a session about OTL blueprints, but I found out that we're not gonna have a…
an hotel observatory booth, this KubeCon Europe, which is…
Sad, sad days, but but yeah,
there may be conversations there at KubeCon, so I will…
Around Blue Plains, hopefully. So I'll be there in…
lciukaj@splunk.com 01:32:26 Dan, so when it comes to… how does… because I believe you have some discussions with… or I'm not sure if you are part of OpenTelemetry governance community, and…
Dan Gomez Blanco 01:32:36 Until recently, but yeah.
lciukaj@splunk.com 01:32:37 Okay, so, so do you know if there's, like…
Is the governance community aware of this project, of OpenTelemetry Blueprints, what we do here?
Dan Gomez Blanco 01:32:47 Yeah, it's one of the priorities for… and it was, you know, as it was discussed, you know, to unplugged, is…
Yeah, it's one of the priorities for the project, right? So, yeah, everyone's aware of it.
But, you know, every SIG is independent, right? So, yeah.
But they're aware of it.
lciukaj@splunk.com 01:33:09 Gotcha, absolutely. I was trying to get some session on Open Observability Summit in North America, which is gonna be in May, about the OpenTelemetry blueprints, but it wasn't approved as well. Then I sent a follow-up email and asking, hey guys, can you include this? Because this is important, but it seems that
Observability Summit is not only about OpenTelemetry, other topics as well, other projects, so it's hard to…
Dan Gomez Blanco 01:33:36 What will be… what I'll make sure that it's included, though, is, like, the… every KubeCon, there is a project update from the…
from the governance committee, so what we… sorry, what… now they… they… they're… they're… they're…
The two is, like, talk through some of the… projects.
lciukaj@splunk.com 01:33:52 Like…
Dan Gomez Blanco 01:33:53 Within the… within… within a hotel, right? And, yeah, I'll just make sure that that's… that that's mentioned.
lciukaj@splunk.com 01:33:58 And that is during the observability Day, right?
Dan Gomez Blanco 01:34:01 No, that's the… that is the KubeCon track… maintainer's track.
lciukaj@splunk.com 01:34:06 Okay, so during the main event, okay.
Dan Gomez Blanco 01:34:10 And, we get, like, actually, we get the last time…
The last KubeCon EU, I think we had… 7…
No, probably 5 or 700 people in the room, so…
lciukaj@splunk.com 01:34:24 problems.
Dan Gomez Blanco 01:34:24 I've ended these ones, yeah.
lciukaj@splunk.com 01:34:28 Good.
Dan Gomez Blanco 01:34:30 And they always put us in a room at the end of it, like, a weird room. But anyway, so, yeah, I'll… we'll definitely mention it.
lciukaj@splunk.com 01:34:40 Perfect.
Cool. Nothing from my side for this call, guys.
Dan Gomez Blanco 01:34:45 Awesome.
Okay, well, have a good rest of the day.
neil yashinsky 01:34:49 Thanks for your fearless. Thanks, everyone.
Oh, bye.
Dan Gomez Blanco 01:34:53 But…
Tiffany Hrabusa 01:34:54 Bye.
