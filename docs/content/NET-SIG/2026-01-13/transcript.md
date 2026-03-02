SIG: .NET SIG
Date: 2026-01-13
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/Q0LPm0pBbbc0U7XMRXTTuPOo_wpwTN5RKjLMxaSiD4IfVyGZfXWeQF3n2-H6j21n.wpIruty_R-sOzelk
============================================================

## Zoom Recording Transcript

**Matthew Hensley** 01:32 Hello.
**Martin Costello** 01:34 Hey.
**Matthew Hensley** 01:39 I assume everyone else will come filtering in here in a minute.
There's… exactly.
**Martin Costello** 01:46 Hey, Virgo.
Hey, Raj.
**Rajkumar Rangaraj** 01:55 Hello, everyone. Hello, Matt.
**Alan West** 02:33 Ew.
**Martin Costello** 02:36 And…
**Rajkumar Rangaraj** 02:57 Do we have any topic for today? I don't see anything in the agenda.
**Alan West** 03:02 Yeah, I just got one thing.
**Rajkumar Rangaraj** 03:05 Okay.
**Alan West** 03:05 I think it's a quick one.
I'd like to push a release, the RC candidate today for the SQL client instrumentation, unless…
Anybody says, wait, wait.
I think we're good. I updated the documentation. Martin, thank you, you did… Some…
Additional good research on the… on the sanitization and adding additional… Stuff there.
I think we're in a pretty good place.
**Rajkumar Rangaraj** 03:41 Great news, like, it's a very long pending one. Many customers are waiting for it.
**Alan West** 03:51 Cool No thoughts from you, Martin?
Yay or nave?
**Martin Costello** 04:00 It's not an A. The only… the only thing I'd say is probably we should do a re… not like this right now, but maybe go through the remaining issues on the milestone, because I had to look before the meeting, there's, like, 4 left over. I know… I know we're not going stable.
But, to see if any of them are done, because I saw Purita did a PR today related to the stability opt-in.
**Alan West** 04:27 Oh, I had not actually seen that, but so yeah, that's a good thing to talk about.
**Martin Costello** 04:32 I think the one he did today was just test changes, but it made me think that we've still got that thing lying around.
**Alan West** 04:40 Okay.
**Rajkumar Rangaraj** 04:43 So, I do see only 4 items over here in the milestone. Is there anything else we have it apart from.
**Alan West** 04:50 Yeah, let's just talk about each of these really fast. So…
The DB operation batch size attribute, I talked to Steve about this a while back, he'd expressed some interest in implementing it.
And the call that I made, assuming people agree.
is… and maybe I should actually note it on the issue, because I just had a conversation with him on Slack.
Was that this is an attribute that is only on spans, it's not on metrics.
So, adding…
Adding attributes to spans later is not a breaking change. Adding attributes to metrics later is a breaking change.
So… I see this as something that we can implement Later, after stability.
**Martin Costello** 05:38 That sounds reasonable to me.
**Alan West** 05:42 And then the stability requirements for the ORM instrumentation, that's… that's with respect to the EF core, and just kind of…
I think us further talking about…
**Martin Costello** 05:53 Oh, yes, I remember now. We weren't going to worry about banking EF.
Okay.
**Alan West** 06:01 So this doesn't affect the SQL client's, path to stability.
But it's still an important issue, because, yeah, getting that EFCore stuff would be… would be great as well.
And… removing the… oh, I already removed that from SQL Client.
So half of that is done, I suppose.
I just… I guess I didn't link it to this issue.
**Martin Costello** 06:42 I guess in that case, then, we can remove the milestone and just update the title.
**Alan West** 06:49 Yeah, that makes sense.
Yeah, so with the… this is the big change with the RC, is that that… this is no longer an option, basically, for people. They'll always get the new conventions with no… with no ability to use the old conventions.
**Rajkumar Rangaraj** 07:16 Go away from the… Why did two of them went away?
Did I incorrectly remove it?
**Martin Costello** 07:23 I know.
**Rajkumar Rangaraj** 07:23 Yes.
**Martin Costello** 07:24 I took the milestones off because they're not for SQL client now.
**Rajkumar Rangaraj** 07:28 Okay.
**Alan West** 07:34 Oh, yeah, this issue.
This, I just… I… I… Don't…
I guess I still have questions about this issue, and I… I don't know, like, there's a few things, thoughts on my mind, like…
One, I think, that's already been discussed on this issue is that, like, oh, you know, maybe we could add an option to,
Allow comments, you know, some option later, like, to allow comments to be in… Sanitized.
query text.
So that's one thought on my mind, but then, really, the big question in my mind is.
for what purpose does this person want this?
It seemed, if I recall, to be related to…
Like, context propagation kind of concerns?
I may be misremembering, but if that's the case, I actually wonder if this is even the right… solution.
Because… Things being propagated for the purposes… things being,
extracted from comments for the purpose of propagation, in my mind, is orthogonal to the idea of sanitizing db query text and applying that as an attribute to a span or a metric, right? Or, I guess, a span.
**Martin Costello** 09:14 The most recent comment on that issue is the… yeah, it's the original reporter there just saying, oh, we just add our .NET method names as a comment to the start of our queries.
To make things easier to track. So it feels like they're just sort of making their own convention.
through comments.
**Alan West** 09:34 And then… Yeah, and that reminds me of my third thought, which is…
they can do stuff with the enrich functionality, right? Like, they… they enrich…
gives them a handle to the SQL command.
And from that, if they wanted to parse out from a comment.
The… some method that called it, or whatever they're doing, right?
They have a way to achieve that.
**Martin Costello** 10:08 I guess they could even just add their own custom attribute.
**Alan West** 10:12 Yeah, that's… that's basically what I'm… what I'm saying with Enrich, you know, they could just say, like, you know, collar, you know?
Colleague method, or something.
Because in a nutshell, like, comments can have any kind of potentially sensitive information, so the…
The decision to strip them from in the sanitization process was just, you know, a very conservative approach to
sanitization, and I think it's the right approach.
**Martin Costello** 10:47 Yeah, because, like, you could imagine there's a user somewhere who writes a query.
Where they put the values of the sprock in the comment, or something like that, and then there's no way to redact… to intelligently be able to parse that and redact it, because it's just arbitrary text.
**Alan West** 11:07 Exactly, exactly.
So then, yeah, I mean, with that said, my conclusion on this one was, like, Not something that…
I think we should consider for a stable release. I mean, we can continue to…
Discuss things on this issue, and…
You know, maybe we'll do something in the future, but… You know, unless…
**Martin Costello** 11:37 The first thoughts on if you did something in the future were, if you had an option, which was, let me have comments.
then you're just sort of, like, you know, foot un equals true.
Yeah. But then if you want to go down that route, then you could have… you could… you could go entirely the other way and go… you could have, like, a full…
AST callback system, where every time it finds a token, it asks you, do you want it or do you not?
**Alan West** 12:06 It's interesting that you say that. That was similar to a thought that I had really early on when I was originally implementing the sanitization and parsing.
Was, offering
An option to just say, like, hey, you know, if you don't want our sanitizer, write your own.
And… and basically just give… like, have a… have a function that's called to do the sanitization and, like, the extraction of the…
Of the, Query summary.
I mean, that's, that's, like, you know, a pretty… Heavy, kind of, solution, but…
That is also something that we could entertain in the future. That could be an additive change.
**Martin Costello** 12:59 Yeah, I feel if you wanted to give this level of control, it would probably make sense to have you let control anything, because otherwise you could, you know, you could have 50 different Booleans. I do want this, but I don't want that.
And then that'd just be a nightmare to maintain.
**Alan West** 13:18 Yeah.
Yeah.
So I think we're in agreement, then, that we… we just hold on this issue, and basically… I mean, we can move it… remove it from the milestone, I think, and… and leave it as a…
Leave it open, I suppose.
**Martin Costello** 13:47 That makes sense to me. I guess if you could, like, summarize
What we said on both of those.
Then, yeah, then that's, like, we've got no issues on the milestone then.
**Alan West** 13:59 Yep, I can do that.
**Rajkumar Rangaraj** 14:10 Thanks, Alan. Is this a blocker, or should we consider this as a…
we can iteratively work on it after the RC.
**Alan West** 14:22 I think it can be something that we can continue to consider. It's not a blocker. Something that we can continue to consider, maybe continue to clarify what this person actually needs.
And… as Martin just requested, I'll write up some notes on that issue.
**Rajkumar Rangaraj** 14:42 Sure. Based off the conversation we had today.
**Alan West** 14:46 But I don't think it blocks going to stable. Like, I think we can push the RC
And assuming everything is good, this is not something that I would…
come back to, or to consider for stable release. I think it can be an additive change later, whatever, whatever may shake out of that issue.
**Rajkumar Rangaraj** 15:10 Cool, then.
So let's go and check if any other topic's been added here.
I'll just make it as today, in that.
No.
So, any other topics, apart from this?
**Alan West** 15:43 That's all I got.
**Rajkumar Rangaraj** 15:44 Good.
**Matthew Hensley** 15:46 I was gonna see if any of y'all are gonna be attending FOSDEM.
Or OTEL Unplugged.
immediately after.
**Alan West** 15:55 Oh.
I've been totally oblivious.
**Rajkumar Rangaraj** 16:00 Yeah.
**Alan West** 16:00 How do we get… how do… how do we get, into that?
**Matthew Hensley** 16:05 Well, it should be a banner on… up on GitHub, but I'll post something in the .NET channel again. In fact, I put one there
Last week in the CNCF.net channel, a link to it.
**Alan West** 16:18 Oh, I can find it there, then.
**Matthew Hensley** 16:19 Yeah, it's in Brussels, the Monday after Frost Dem, which is 2 or 3 weeks away?
**Martin Costello** 16:28 It's 3.
**Alan West** 16:32 Oh, it's an in-person thing.
**Matthew Hensley** 16:34 Yeah, yeah.
**Alan West** 16:37 I won't be there.
Cool. Are y'all, any of you all going?
**Matthew Hensley** 16:47 I will be in attendance, currently, I don't think you are able to come, Martin.
**Martin Costello** 16:54 Yeah, it reminds me, it's like, I won't be here… there's a good chance I won't be here the next 2 weeks, because I've been called up for jury duty.
**Alan West** 17:03 Oh, congratulations.
**Rajkumar Rangaraj** 17:05 Which means that if that is the case, I will not be attending FOSTEM.
**Matthew Hensley** 17:12 Well, hopefully you can sneak away. Yeah, if y'all aren't making it, I will…
bring back any relevant notes. I think the plan is most of the GC and TC should be present.
And they're wanting to lay out a roadmap for 2026 and beyond, kind of setting the direction for the project going forward.
**Rajkumar Rangaraj** 17:39 We will hear from you, Matthew. I don't think anyone is going from the…
Here, any maintenance or approval from here.
**Alan West** 17:49 I suspect that my colleague, Dan Gomez-Blanco, who's on the governance committee, will
Probably be there? I actually haven't talked to him about that.
But, you probably see him.
**Matthew Hensley** 18:03 If you don't mind poking them just in case, since you weren't aware.
Yeah. I would assume it's come up in their meetings, but if for some reason it's not,
This is gonna be one of those interesting, problems to solve, because lots of people don't know about this, but it's been advertised since November or December.
So, probably just missed for the holidays, but yeah.
But yeah, I'll bring back whatever, seems relevant.
**Alan West** 18:33 Cool.
Thanks for the heads up.
**Rajkumar Rangaraj** 18:38 Let me move on to the report you see. So, all the changes related to the TLS and the MTLS support got merged last week.
So we don't have anything pending from that aspect, so in that way, we could say that OTLP is ready for the next release, if whenever we feel like we can consider that.
So…
apart from that, I saw, like, Martin taking a look at this, PR, the last one. Today, I've also taken a look at it. I raised through a few questions, and still the…
PR summary is not updated. I've asked them to get that done. So, change-wise, I had a glance, and it looks pretty neat, and it's not impacting any of our current
the flow. So, in that way, it's fine. So, my only concern is, whatever the public API they have, even without that, we can,
get this PR merge, and it should work as expected. I've asked that question, why they have it.
So, let's wait and hear back from the contributor to see how he wants to tackle that. But whatever the PR public API that's been added, it's the best practices normally in the .NET, just to expose the options so that
They can take, the options can be directly,
shared through the public API itself. That's what's been done over here. So…
**Alan West** 20:16 Thank you for reminding me of this. I actually did begin to look at this PR,
And I, I… Wrote down a couple of questions, but I hadn't actually commented on the PR.
These constructor overloads, my first question was, these overloads, Why are they necessary?
**Rajkumar Rangaraj** 20:35 Yeah, I already left the same comment, one in there. It's not needed at all, like, based on my,
Like, but it's based on the best practices, that's what I'm seeing, it's been exposed, but that's my, why they need the constructor is the question, especially, I've asked.
**Alan West** 20:56 My other question about it, was… I mean, kind of stemmed from the fact that, like, I didn't think that the constructors were necessary, was that
The way that it detects whether,
It's on, like, a platform that supports threading or not, is that it checks, like, whether the thread pool has one thread.
**Rajkumar Rangaraj** 21:18 Yeah. And…
**Alan West** 21:19 Anyways, I was just… yes, yes, this code here. I was just looking at this, and my question about it was, like.
is that actually… is this actually a valid way to detect what is… is it possible for, like, the number of threads to increase later, or something? Like, get max threads to return something?
Later at runtime?
I just don't know. Like, I'm not…
**Rajkumar Rangaraj** 21:44 Let me do something, right? I'll just check internally if I can reach out no one, ask him to take a look at this threading helper, only this part for us to provide a clarification. I'll check with him if he has bandwidth to do that review for us.
**Alan West** 22:01 Okay. The… yeah, because my original, like, question that I posed on this PR a long time ago was basically, like, can you just detect the type of platform that you're on? Like, if Blazor is one of the use cases, like, is there just, like, a way to check, like, the environment and
definitively know that it's Blazor.
But it looks like they went this approach, which may be totally cool and valid, I just… I'm just not super confident in myself.
**Rajkumar Rangaraj** 22:31 That makes a lot of sense, also. So I'll just go ahead and… even I had a few questions where I needed to reach out Noah on this one. I'll ask him. Even before engaging, I thought I'll wait for the contributor's response on this one.
Maybe I'll ask the contributor to join one of our SIG also, so we can directly question them as we went through this one.
But this one, I'll get help from the .NET team to see if that's a reliable thing to detect.
the… A blazer part.
**Alan West** 23:06 Cool.
Alright.
**Rajkumar Rangaraj** 23:13 I think that's all the… that is another PR, I don't know how many of you are taking a look at it, but at least I'm not a big fan of that, though. Someone wants to change the console exporter format.
Not a big fan of it, I'm not a big fan of it, but if every other… I say that with an additional option, we can… he can try that.
**Martin Costello** 23:38 I…
**Rajkumar Rangaraj** 23:39 Nope.
**Martin Costello** 23:39 I saw it, but I didn't…
Review it in much depth, as it…
At first glance, it just seemed to me a bit overcomplicated.
**Rajkumar Rangaraj** 23:49 Yeah.
**Martin Costello** 23:50 Like, it's a lot of code being added to be looked after in an area that doesn't have much test coverage.
For something that… There doesn't seem to have been any demand for, apart from the person who's added it.
**Rajkumar Rangaraj** 24:04 Yeah.
So, that's where, like, I don't know, like, I wanted to hear from… I've said my view, but CJO is an approver, he has a different view. I want to hear from the other maintenance and approver here, what's the view, and we… should we encourage and move this, or just tell the,
user that we are not accepting it, because there is a lot of work. Keep on doing the work.
**Martin Costello** 24:32 I think he's also been chasing to get it reviewed, because he's asked in the issue, who are the maintainers? And he asked in Slack, who are the maintainers.
**Rajkumar Rangaraj** 24:43 So the thing is that here, like, it's a slight… I could have told him we need to create an issue to brainstorm. He created an issue, but unfortunately, we did not respond to him, and
Now, for…
quite a long time, and then he went and created PR, so we cannot complain him that he did not try initiating a discussion earlier. So, probably, like, taking a look at what he's trying to propose and providing our view would help in this case.
**Alan West** 25:19 Yeah, I think this one looks vaguely familiar to me.
And I… and I… this is… and I recall, I think this was part of the discussion, But…
I think that… The specification has… like, A recommendation for exporting.
**Martin Costello** 25:40 The ability to export, like.
**Alan West** 25:41 JSON format.
**Rajkumar Rangaraj** 25:42 say it is not, because that's what I felt and did it, but Sijo says that
Spec made it evidently clear that,
**Alan West** 25:52 the output from the console is not guaranteed. No, that's… yes, that's true. I… I agree with what CJ was saying there, but I think that the spec also went on to…
I could look it up, but I… it would take me a bit to find it. I think that there was something…
A recommendation to implement like, JSON format, like, export.
**Rajkumar Rangaraj** 26:16 Correct.
Similar thing has happened earlier, the discussion over here. YAML versus JSON and everything. Yeah. I recall, yeah.
**Alan West** 26:24 And so something like that, you know, seems like it would be a positive contribution.
**Rajkumar Rangaraj** 26:30 Yep.
**Alan West** 26:31 But, yeah, outside of… If it's just, like, changing…
the made-up, the thing that we just made up, the format that we made up, which I personally don't like either.
Like, I think… I think we… we… we took a really, kind of, like, just quick and dirty approach to it all.
But, you know, I wouldn't want to change it, though, unless we really, like, deeply considered. And I'd probably…
if I were to go down that approach, I'd probably want to, like, drive the conversations beyond just this SIG, right? Like…
maybe look at what the collector does in its output. Like, I… I've… I look at… I look at the collector output a lot when I'm supporting customers and so on, and I actually kind of appreciate their console exporter format.
But I'm sure that other languages have their own formats, too, and I haven't looked at those, and maybe there's some good things to see.
from other languages as well. So that's the kind of, like.
I'd want the conversation to be bigger than just… just an issue within our repo, basically.
**Rajkumar Rangaraj** 27:38 And then, like, your thought, if you could… whatever your thought, you don't need to get inside a review that, Pierre. Whatever the thought you shared, if you could just add a comment here, that would be helpful.
**Alan West** 27:50 Sure. Yeah, this is issued as, what, 6391? Okay.
**Martin Costello** 27:54 Another thought I had was because I think the contributor mentioned this being good for learning.
something that occurred to me was, like, it wouldn't be much effort to add Aspire
to something. And there's, like, you can just have people look at the Aspire dashboard locally and see
How telemetry works that way.
That's a… that's another possible approach you could do without having to,
Add a whole new set of functionality to the console exporter.
**Alan West** 28:25 Yeah, that's a great idea. And there's some other tools, too, that I personally use, like the OTEL…
TUI, the terminal UI? Have you played around with that at all?
**Martin Costello** 28:38 I haven't used that myself, no. And then, of course, we've all got our own opinionated APMs as well.
**Alan West** 28:44 Yeah, totally. Yeah, exactly.
But just running things locally, sometimes I'll use,
hotel TUI, it's, just a way to, in the terminal.
See the telemetry that your apps are sending.
It's pretty neat.
**Rajkumar Rangaraj** 29:01 Yeah, even very clearly, we called out, like, CJ also very well called out this one.
He's worried about the misuse of this exporter, like, it's for learning purpose. That's what I feel, like, at least this console exporter, whatever, we have it as for that, not for any production usage, or really used in the application monitoring at all.
Cool. These are the two PRs I wanted to have a discussion, because, like, there is a… we see a good motivation from the customers to get this merged, so it's, like, these two deserves our, like, attention.
That's all I think we have it here, unless I'm missing something.
**Alan West** 29:59 Nope.
**Rajkumar Rangaraj** 30:00 Good.
Thank you, everyone.
**Alan West** 30:05 Alright, see y'all next week.
**Martin Costello** 30:08 See you next time.
