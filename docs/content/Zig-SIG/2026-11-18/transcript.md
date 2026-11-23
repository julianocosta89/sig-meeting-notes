SIG: Zig SIG
Date: 2026-11-18
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 05:46 Hello?
Yash? You there?
**Yash Raghubanshi** 05:54 Yeah, hello.
**Francesco Gualazzi (OpenTelemetry)** 05:56 Hey, how long have you been in the meeting? I… I was not looking at the tab with my… with the meeting, so I don't know if you were here for… Longer, and we're waiting for me to start.
**Yash Raghubanshi** 06:11 Yeah, so, hello, sir.
This is my first meeting, yeah, so…
**Francesco Gualazzi (OpenTelemetry)** 06:17 Great to have you here, honestly. I guess it's pretty late for you, no?
**Yash Raghubanshi** 06:21 Yo.
**Francesco Gualazzi (OpenTelemetry)** 06:23 It's almost tonight, like, 8pm or something, maybe more, maybe later.
Okay, so welcome. Well, we don't have anyone else in the meeting today, but usually Antoine and Giovanni are here.
And today, I think I'm the only one among the maintainers, because they are both probably busy.
And so, if you want to discuss the PR that you sent, and why I requested the changes, I read your comment earlier.
And I probably agree with you that we should close this one and do it… do another one, maybe in smaller steps.
But yeah.
Yeah, let me know all your thoughts.
**Yash Raghubanshi** 07:13 So, let me open this… People like… So, you have said that the… there was a changes in allocator, right? So, I've changed it.
But… Exactly the internal collection are unmanaged and initialized empty.
So, you have said that if allocator is not used, we might also… we remove the parameter, but why?
I didn't get the reason.
**Francesco Gualazzi (OpenTelemetry)** 07:53 Yeah, Luke, I'm sharing my screen, do you see it?
Do you see the tab? The tab that I'm sharing? Okay, so… Mike… well, maybe I make it a bit bigger.
So, in this PR, the comment they left here… Where's that?
Here.
You see, what happens here, a locator is just discarded, Right? So, along this function.
This… this parameter is never used.
Okay. You see, it is only assigned to the nil or discard operator, and thus I said, yeah, well, we better just drop it, because usually.
when you do that in Zig, when the init does not have an allocator, so the allocator does not sit indestruct.
Right? That means that you will have member functions, like in this case, you see, you have init that does not have an allocator, and the init does have the allocator, right?
So, this is a member function, because the first argument is a… mutable pointer to the same struct where it is declared. And then the allocator here is used to de-unit the structures that are populated inside, so these… these fields of this track, right?
That means that somehow, when these are populated.
they are always past an allocator, right? In fact, unmanaged here means that it is not a release that gets initialized with an allocator. You are free to Do operations on that array list with any allocator you want, but the downside of that is that you have to keep track, or Consolidate the way you allocate memory.
Across… across all coal sites, right?
So, this is something… very unique to Zig, you know, because allocator is just one other parameter. You know, like I.O. is in some circumstances.
So that was my comment here. But, going back to my actual review, Yeah, the point is, and thank you for addressing also the co-pilot review here, which was a lot, but the point here is that maybe I'm misremembering how it works, and I have to go back to it, but we already have multiple readers.
No, you are saying, and I have to check because I haven't really checked, that right now, if someone configures multiple readers on the same meter provider, they will clobber each other, right?
**Yash Raghubanshi** 11:03 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 11:04 I think we had a test that asserted, you know, to prevent this, but probably This is not valid anymore, since now we… Let's say, squash, the data points, On every collection cycle, which… I do remember now why I did it like that, I designed it like that in the first place. So, it was intended to keep all the data points all the time, so having this Unbound memory role.
And the reason was that if you would re-export, you would need to re-export all the data points with the different aggregations, you would be able to Recompute the entire aggregations from the start.
I don't… again, I hadn't envisioned the… the sudden, you know, it's so… so much memory growth, you know, for those data structures, which is not sustainable, especially if you think about, like, a database or a very long-running process. And I thought, initially, my idea was that when we do a collection cycle that can have multiple readers.
Then, the output of… The data points, the raw data points, is just, say, leaving the instrument.
And it's then handed off to the readers.
And then the readers, they do their own logic, and they produce their own aggregations, and blah blah blah.
Now, I would love to see this design idea contextualized in the code, right? So, maybe I should rephrase it a bit better, and Yeah, and also the pointer Constanio Park, I thought it was unnecessary, because Is this just needed here because you don't want to re-import on a circular dependency, but… AI Zig does allow circular dependencies, across modules, but… You know, in general, what we want to do is try to keep API and SDK separated. The metrics are not like that. That's my fault.
Because I… I was lazy at the start, and we never, and we never… What?
Did you say something?
**Yash Raghubanshi** 13:37 No, no. Continue.
**Francesco Gualazzi (OpenTelemetry)** 13:39 Because I was lazy, and I was, not considering this, this thing.
from the get-go, also because, yeah, interfaces in Zig are manually… done. You hand-roll your own interfaces, so you write the struct and the V table, and then the implementations. You don't have any, say, built-in construct, like in other languages, like traits or interfaces, but Yeah. So, the problem still stands, right? Because, as you said, like, you know, like, this… this is true. Yeah, okay, so I recognize this is true.
And thank you for following up on that.
I just didn't… Think that this… PR was… the correct step forward in the right direction. So the next… a good step in the right direction, right? So… Let's… let's probably close this one.
Okay.
But this is still open, right? Yes, so I…
**Yash Raghubanshi** 14:42 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 14:42 What I can do, probably… well, what you say, given the core problem of unbound, every good Israeli solve, okay, no, this is… this is partially done.
Here are two ways forward. Yes, close this PR, Yes?
and defer multi-reader storage to separate OpenTeameter SDK? Yes, that's… that's… that's what I would do as well.
record temporary negation fraud.
That one, that one, that one?
**Yash Raghubanshi** 15:10 That one…
**Francesco Gualazzi (OpenTelemetry)** 15:10 Close metric seems to install everyone.
I guess, I mean… Okay, yeah, maybe we can close this, and tackle proper multilateral resolution as part of it. Or maybe we just close this one and create a new one that is just for the… multi-reader.
data isolation, which might end up Allowing us… which might allow us to also split it out, right?
**Yash Raghubanshi** 15:46 Okay.
**Francesco Gualazzi (OpenTelemetry)** 15:47 Otherwise, move pipeline and view processing into SDK. This is… yes, this is what I… this is what I should have done from the start.
But I… I was naive, say.
Yeah.
Yeah, yeah, yeah. Keep instruments completely clean, and let the SDK meet a provider metric here, SDK storage manager… yeah, I… this is also basically what I would like to see happen in this new issue that I'm going to create very soon.
Yeah. Okay. So I will reply here, and likely I will close this PR, if you don't mind. Sorry for that.
But, I think it's pivotal that, in order to go… happily on the alpha release milestone that I'm thinking we do probably early next year, so January. I'm hoping that we fix all the issues by January next year. It would be very nice if we would start 2027 with an alpha release of the Zig SDK, official Zig SDK, because we recently merged the gRPC compression support, so…
**Yash Raghubanshi** 17:03 So, basically, I'm start learning about milestone, like Alpha, starting. This is my earliest days, so I look into the depth, so… From start 10, I can start on…
**Francesco Gualazzi (OpenTelemetry)** 17:16 Okay, so do you have the milestone in front of you?
**Yash Raghubanshi** 17:20 So, like, I've… I've added one issue in that, like, is a…
**Francesco Gualazzi (OpenTelemetry)** 17:27 Let me pass the link here real quick, so we know… what we are looking at. Or maybe just share my screen again.
Problem is that… Screen share on the browser is very memory-hangry.
4K monitor, and I… Hesitant to do that, but… Issues, maybe this one.
**Yash Raghubanshi** 17:52 Excellent.
**Francesco Gualazzi (OpenTelemetry)** 17:54 Okay, you see, you see it now also in the meeting. So, this is everything that we have, that we need to complete for the alpha release, at least at this stage.
There are two items that are still not tracked here. One is the conformance with specification 1.62. Right now, we are on 1.48, we are very behind.
And Giovanni did already a… oh, no, he's already here, sorry. Yes. So this one is very big.
Because we have a lot of features, we are behind on lots of features, but… I think… You know, we are not in a… Bad, bad, bad shape.
Yeah, we… we have, let's say, we have a clear path for this one.
Also, because we don't want the development thing, so for the alpha release, just the stable features are okay. So, okay. And this will be handled mostly by the maintenance, but if you feel like you have cycles to… To take some of those, If it doesn't… Then… We closed the compression earlier today.
This one is, from you also, you opened it, thank you for doing that. I think I have the solution, ready, it's probably a couple of lines changes, it's… I mean, it is not.
Too big, so it's gonna land very soon.
This one is for the SAMConv module, SAMConf package, right?
And, and this is probably also the biggest one.
For the documentation, we, Giovanni, Juan, myself, Jacob, and Emal, hopefully, we will have to talk with the… GC liaison, like, Alolita and Josh from McDonald, in order to get guidance on, like, on how to open the PR, but before we open the PR to the OpenTelemetry documentation, the telemetry website repo.
I would like that we close everything else, so we don't have bugs, we don't have huge bugs, we don't have huge missing features, so basically this is the last one to be done.
And, yeah, and this one also is, like, a small change in the configuration of OTLP.
I also… this one is also my fault.
**Yash Raghubanshi** 20:25 Right.
**Francesco Gualazzi (OpenTelemetry)** 20:25 I… I didn't… there's a to-do written by me in the OTLP exporter that says, we will figure it out later, but okay, I guess this is easy to address.
And then there is this new one, which I'm going to create with regards to… isolation of multiple readers, so the concept of the pipeline that you created is fair, I mean, I… I don't hate it.
But the way it was delivered, so everything inside the API module was… Not… not the right thing, again, I will not try to… repeat myself, but again. So I will create one new issue.
We'll put it here, maybe assign it to you, if you don't mind, if you want to work on it, let me know. We can always sync in Slack.
And then I will just, you know, work on the other issues, like… spec, this one on the SAMCOM, this one, for sure, I will assign to.
**Yash Raghubanshi** 21:21 Yeah, so…
**Francesco Gualazzi (OpenTelemetry)** 21:24 This is… this is super easy.
Okay.
Oh yeah, that's basically it.
Any tools?
I'm filling in the… do you have access to the… Agenda document that is linked in the meeting invite?
**Yash Raghubanshi** 21:50 Which one? I guess…
**Francesco Gualazzi (OpenTelemetry)** 21:52 Goodbye.
So, the meeting invite here has a document link, a Google document. Let me also.
**Yash Raghubanshi** 22:03 Josh.
**Francesco Gualazzi (OpenTelemetry)** 22:03 Is it here in the meeting chat?
I don't know if you've seen it.
This is where we track everything that we discussed during the meeting, and you can add yourself here, because.
**Yash Raghubanshi** 22:17 Cool.
**Francesco Gualazzi (OpenTelemetry)** 22:18 Yes.
Feel free to add yourself here, and I will, Add the sampling that you need.
Okay, so… It's true.
It's done.
Taking notes, so… Then what else? I… Sad, yeah.
But it is… OS… It's progressing well.
Yash… Videos.
Excellent.
What else?
Did you like, I would walk insofar, so… You know, have you enjoyed, contributing to the repo? Have you…
**Yash Raghubanshi** 24:08 I've learned a lot from this, like, it's my first time, like, I've started somewhere else.
But I didn't cope up, so I started here as… so I learned a lot.
And I enjoyed it.
**Francesco Gualazzi (OpenTelemetry)** 24:25 Good, good.
I mean, I also have a mentoring program, I don't know if you're aware, but… If you would like to go through some of the components more in detail, we have, The, slots in my… Calendar that are assigned to… helping, contributors of the Zig Autel SDK to… Understand, you know, how… why certain things are done and how they work, even in the Zig interim. Because I've been using Zig for 4 years now. It's, I want to try to spread as much as possible the knowledge of Of the language and its… capabilities, right? Because I really love seeing.
**Yash Raghubanshi** 25:19 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 25:20 Okay.
I will send to you the link in Slack, maybe you can book a slot with me if you'd want, or no, if you don't want, that's fine also.
But thank you for all the contributions that you are applying. I mean, a lot of things have been adding great value, and I have to tell you also, because you were not in the meeting before, but Thanks to your fixes, I was able to deploy the first… production application?
with OpenTelemetry metrics exported to an OpenTelemetry compatible backend.
And it's working, like, greatly. So, thanks to you, thanks to Antoine, thanks to Giovanni. So, we have, out of that application right now, we have traces and metrics, no logs, but, it's still, you know, a great satisfaction, because I had never deployed Zig in production, and now I was able to get the chance to do it, and it also works fine Thanks to your fixes and your issues that we tackled, so… yeah, the SDK, I feel like it's working pretty good.
for many use cases. There are still a lot of bugs, I'm sure, but.
**Yash Raghubanshi** 26:39 Yep.
**Francesco Gualazzi (OpenTelemetry)** 26:39 We will, catch them, and we will fix them.
time, and…
**Yash Raghubanshi** 26:44 And… Thank you, thank you, sir. Thank you to HyperTrust.
**Francesco Gualazzi (OpenTelemetry)** 26:49 Yeah, always happy to see more contributors jump in, and… Okay, I don't have anything else, Any… you want to discuss about something, You want to improve, or, you know, some ideas, whatever you want, this is a free space for you.
**Yash Raghubanshi** 27:12 So, I didn't prepare for much as, like, I joined it.
**Francesco Gualazzi (OpenTelemetry)** 27:19 You know, maybe next time, yeah.
**Yash Raghubanshi** 27:22 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 27:25 Okay, thank you for joining, Dan. I guess we'll call it a meeting. Enjoy your night.
**Yash Raghubanshi** 27:32 Yeah.
Thank you.
**Francesco Gualazzi (OpenTelemetry)** 27:33 In fact…
**Yash Raghubanshi** 27:34 Bye. Bye, bye.
