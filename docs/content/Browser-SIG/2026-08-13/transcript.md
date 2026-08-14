SIG: Browser SIG
Date: 2026-08-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Cleo Schneider** 00:30 Hey, Jared.
**Jared Freeze** 00:32 Hey, Cleo, how's it… how's it going?
**Cleo Schneider** 00:34 Going alright, how are you doing?
**Jared Freeze** 00:37 Good.
Why is this window so small?
Somebody on the SIG yesterday said computers were a mistake, and that is absolutely the warning.
I'm having.
**Cleo Schneider** 00:47 Oh, no.
It's relatable content.
**Jared Freeze** 00:53 Hey, Ted.
I might Slack you. I think I'm going to the Big Island in September.
See if there's any spots I need to see.
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:17 Elsia, is it your first time?
**Jared Freeze** 01:22 In a really long time.
I went to Kona once as a kid to see my uncle, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:28 Yeah, I got my list, I sent people, for sure.
Is it too?
**Jared Freeze** 01:35 Appreciate that.
Hey, Wolfgang.
**Wolfgang Therrien** 01:39 Hello, hello.
**Jared Freeze** 01:41 Welcome home.
**Wolfgang Therrien** 01:44 Thank you.
**Jared Freeze** 01:52 Pretty sure Waco's coming.
Did you guys see the note about stacks, by the way?
I don't think we need the group for that, but, Trask posted something about using stacks on forks, which I guess they're enabling now, which I thought was kind of nice.
Don't know exactly how that works, because you can't set… a base, but I guess they're just enabling it for, like, the same fork.
Where did he post that? I think it's in the maintainer's channel, but… I can cross-post it if I have it saved somewhere.
Okay, we're probably good.
Let's see… David, do you want to get us started?
Still on mute?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:28 David, you're muted.
**David Luna Bistuer** 03:37 Yeah, sorry.
I'm not talking to you.
making a lot of noise, so I was kind of pushing them out. Okay.
Okay, I think that maybe, this topic is going to be fast.
There is this… so, long ago, we made all these issues to move instrumentations, and one of them was the… Document load.
But after having a second look a couple of days ago, yeah, it was last week.
I know that we have this navigation timings, and I see that we are getting the entries from navigation, and maybe, I don't know, just, For me, raised the question about, okay, maybe with navigation timings, we have all the information that we need for that, and then maybe we can just, you know.
Just if we get the document loaded, just get the, The information from hard navigations, which could be, a similar thing. I didn't even go in-depth, so that's one of… in my list.
on actually comparing the two of them. I think, Jared, you mentioned that in the thread.
About having a good comparison of both instrumentation, see if they actually get the same information, and… And maybe then decide about that, so that's on… I guess, maybe that's on me, if anyone wants to join on the analysis, I'll be… I'll be happy.
But yeah, that's it. So, what do you think? Do you have any thoughts about document load discrimination? If anyone is using that.
I think DocumentLot, it's creating a spans, but the same, it's using navigation timings, and then creates a span with the timings that it gets, so it's kind of faking the spans, somehow.
**Jared Freeze** 05:20 Yeah, I definitely have thoughts, but go ahead, Martin.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:24 Yeah, I was gonna say, like, the only use case that I can think of that might still be valid is if you have a backend that serves a page, and we propagate the context from the back end, like, through the MetaTech, or, you know, the… That mechanism, and then you want to display A span as part of the trace.
It starts from the back end, and, like, the end result is the load time in the client.
**Jared Freeze** 06:00 That's actually a good segue. So, in the W3C meeting, there is a proposal currently to put performance timing information in headers that are readable in the browser.
that was the coolest thing ever, because it means that you can pull timing information before your script lifts. So, that is actively being pushed, and everybody wants it. So, I think it's actually higher on the list than something like async context, which is very, very hard to do.
Performance timing is just moving it up in the source code. Not to trivialize browser makers, but… I think they know how to get there, so… That's… that's one note. The other one is that we, like, on the vendor side, we actually have dock-loaded instrumentation, and I spent a lot of time working on determining if something is cached or unreadable.
So, we have a long chunk of code that actually looks through file sizes and does all these other things and marks things as cached.
I would like to get that moved over. I think that plus… the propagation, like, if we were able to mash it all together, I feel like navigation timing is still… Probably a good name for what this does.
And we may even want resource timing to get that helper as well, because, you know, it reads body size and does all these things.
So… I would like to upstream that, if anybody has thoughts about that.
It might… it's a little bit different, but I think… at least having a draft PR to look at, just to see the differences, I think would make it a little easier, that way I don't have to send, you know, source to our repo, which… You know, it's not what we do, so… Is anyone opposed to that?
**Wolfgang Therrien** 07:50 No, I think it sounds like a very reasonable idea.
**Jared Freeze** 07:54 Cool.
Okay.
Cool. Cleo?
**Cleo Schneider** 08:17 Yeah, so, thanks everybody for chiming in on the onboarding doc. I think there's been some really good stuff in there, and one of the things that… that came up, is I added a little snippet about a GitHub workflow, and it sparked a lively discussion. Should we… instruct people on how to, use Git, should we, recommend rebasing or not? And there… and so I think it sort of, it brought to light that maybe we should talk about those conventions and, and actually document them. And so, I would just want to open it up. David, I know you had a bunch to say about it, and then, we'll make some decisions.
**Jared Freeze** 09:05 I can start by quoting Trent.
Anyone who rebases after they get a review should be banned from the internet.
**Trent Mick** 09:15 Oh, force push and rebase is different, right? Oh, I guess that's what you're talking.
**Jared Freeze** 09:19 I mean…
**Trent Mick** 09:20 Yeah, yeah, yeah.
**Jared Freeze** 09:20 Same idea. Same idea.
that's… that's my personal thoughts, because if you refactor, you can lose the line number. So it's a little different if you're able to keep code modified on the same line, but if you, like, move a function, the comment just kind of gets disconnected. I think that's the issue. Small things like, you know, typos or something that stays on the same line. I find that's pretty clean. Sometimes those stay intact, but when they don't, it gets pretty difficult to read. When you come back to view.
you know, view new changes, it's just everything again. That's kind of a bummer. That is the reason why It's, like, rebase to your heart's content and forced push, until you get a review, and then after, you know, just live with the fact that it's totally ugly.
Commit to have an update, merge, commit.
That's my two cents, so…
**Cleo Schneider** 10:15 Interesting.
I… I differ from that. I'm, like, a rebase stan forever, but have, like, very… on our team, we have very strict, like, code commit hygiene practices, and so after you've gotten a review, if you're making changes, you have an explicit commit that are the review updates.
So, people can continue to sort of see new changes based… commit by commit.
different, different strokes, you know? I'm happy to do whatever.
But what do other people think? I want to hear what other people think, too.
**Jared Freeze** 10:57 I mean, we should probably make a distinction between squashing, You know, enforce pushing.
you know, I think of force… bush, I mean, I can live with that. I think squashing is probably the most destructive thing.
But yeah, is anybody else?
**Wolfgang Therrien** 11:16 I think it is… oh, sorry, go ahead.
**Joaquín Díaz** 11:19 No, go, sorry.
**Wolfgang Therrien** 11:21 No, I was just gonna say, I… I would love to be able to preserve, like, comments. I don't have a strong preference for the mechanism, but being able to come back and see what folks were talking about in context, I think, is important, especially for a largely asynchronous workflow with a lot of different parties. I think that is… Different than, you know, a more cohesive set of folks who maybe all work on the same codebase at the same… at the same company.
**Joaquín Díaz** 11:54 I was about to say that as long as we squash at the end of a PR, I'm fine with any approach.
**Cleo Schneider** 12:03 Okay.
**Jared Freeze** 12:05 Okay.
**Cleo Schneider** 12:06 I think you and Jared are on the same page, so why don't we go with that? We'll say you can, like, rebase to your heart's content once we have reviews, do a merge so that we retain comment history and context. I'm cool with that.
**David Luna Bistuer** 12:21 Nobody's good.
**Jared Freeze** 12:23 Yeah, okay, cool. So…
**Cleo Schneider** 12:28 Sweet, let me… Type that in.
**Jared Freeze** 12:31 You can go right ahead.
**Cleo Schneider** 12:44 Cool. And then, Jared, you commented on this after I, after I had added that line item in here, and so, which is around our… around issue triage. The remaining to-dos are kind of issue triage, which, Martin, you had also asked a question about. It's like, who is this for?
Yeah, there were a lot of comments. We'll have to go to the bottom.
So, yeah. And my response here is basically, I think both? Like, so the comment here, we can read it, is it for new people, or is it for maintainers-approvers?
And I think kind of both. We want to set expectations for when you submit a new issue, what can you expect, and do you need to take any actions, and for those that are reviewing, if you're new to reviewing, this is what we expect from you.
Do folks agree we want to include that in this… in this… section, it's… It's our stuff, so, like, whatever… whatever folks… Think is helpful or not helpful.
**Jared Freeze** 13:58 I mean, we could… I mean, we… maybe it's… maybe it's just a title change, and just say, like, filing issues, and then maintainer issue triage, or something like that.
Okay. Should we just have two sections? I mean, it's in contributing, right? So… Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:18 Yeah, I think it's definitely helpful. I think, you know, setting expectations to contributors, like, since it is in contributing doc, what to expect, and what kind of… what things we might… Ask for, or… What maybe, what criteria we would use, like, to accept something or not accept something?
That's useful for sure. And then maybe, like, listing… Like, some of the common labels that we use for, To, like, signal, like, what we need, from the… As the next steps.
**Cleo Schneider** 14:56 Cool. Yeah. Yeah, I'm happy to add that. I don't necessarily have all that context, so if some… if I could get a buddy to help… help me understand what things should go in there, that would be really helpful.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 15:10 I can, I can help with that.
**Cleo Schneider** 15:12 Awesome, thank you, Martin. And then the last one was documenting our tool chain.
Do we have a consistent toolchain?
**Jared Freeze** 15:24 When you say toolchain, are you talking about, like, the build system? Like, how… like, the actual construction? I wrote that. I… I… yeah, I can… I can leave notes about, you know, TS down and things like that.
Okay. Yeah, you know, ESM only, all that good stuff. We, we, we also have… There's been some discussion, too, on, you know, browser support and things like that. They're all in flight, I mean, it's really just a time problem.
finding the time to do all this stuff. But yeah, I can absolutely add that to… like, some sort of technical document. I don't know if it belongs here.
I mean, it's more like background than anything.
So… I'm not sure where it should live exactly.
**Cleo Schneider** 16:10 How about in the short term? I'll remove it from here. There's, like, plenty of stuff in this doc, and maybe we can… file it as a to-do. I don't think it's, like, the most pressing part of this.
**Jared Freeze** 16:25 I do think it's… I do think it would be a good thing to let people know I mean, the tooling that… consumers use is really important. Like, we don't support CommonJS at all. I think those things need to get called out. How we construct things is slightly less important.
But yeah, I think we should… we could do both, you know, if it's useful.
**Cleo Schneider** 16:49 Okay.
Sweet. Yeah, I can take that as an action item to follow up, and I'll… and we can talk about where it should go, Jared, and then I'm happy to make those… make those updates.
**Jared Freeze** 17:02 Okay.
**Cleo Schneider** 17:04 Sweet. Awesome.
And then there was some churn, I think, around the NPM stuff, and the Node and NPM versions. Joaquin, I think you left a comment, we have an NVMRC.
Yeah, what do people think about what we want to go What we want to tell people about how they should install Node and things like that.
**Joaquín Díaz** 17:29 I don't know the exact words we should use, but I think we should say that we should encourage people to using NVM by using NVM use… It's just a way of avoiding the bring me to go stale once we update node. If we say we use no XYZ, then we have to update also that one, we update node. And we also… we always update, so this is… Start cut. But yeah, it's a small note on that.
**Cleo Schneider** 18:01 Okay.
Awesome.
**Jared Freeze** 18:04 Yeah, it's in… so it's enforced here. Not everything reads this yet, but newer… I mean, it's kinda… like, chicken and the egg, like, NPM reads this. The newer NPMs read this to let you know you have an old NPM. But, But yeah, this is… this is a hard requirement, because… of an issue with lock files, I think. Trent and I were packing on for a long, long time.
There was just an issue with, peer dependencies or dev dependencies, so… This is the hard requirement. I think… node is less important. Yeah.
So, you know, a lot of people are using other tools as well, like FNM, which I think is… nice and fast and new. So, I mean, we can leak out to some of those things, but, But yeah, I agree with Joaquin. Like, the copy-paste stuff might be… a little tough, and I think linking to the Node homepage Might not be enough info, so…
**Cleo Schneider** 19:09 Okay.
**Trent Mick** 19:10 If there's a logical best place, you can just document The reason why… There's a base version of whatever.
when there is, so as… as Jared's saying, in this case, there's a solid reason why we have that minimum version of NPN.
Because of package lock shenanigans, but for note, it maybe isn't important right now for the bill tooling, of which.
I don't think you can have a comment to an NVMRC file, so you can't put it there.
Can't nicely have a comment in the package.json file, you probably don't want to be doing.
acts on keys, so, yeah, if it fits in the stock.
**Jared Freeze** 19:48 I mean, the CoreJS doesn't have anything, right?
**Trent Mick** 19:55 For a repo?
**Jared Freeze** 19:57 Yeah, the core repo doesn't have installation for Node, it just says use node.
**Trent Mick** 20:02 Just says use node, yeah. And, I mean, we just have engines, right, for the minimum version, and then… The hope and assumption is that you can do all of the build steps with any of the versions of Node that are supported, but I'm not sure that's always the case, so sometimes some of the build tooling assumes you use the latest version of Node and then run tests with an earlier version, but… Yep.
**Cleo Schneider** 20:30 Okay.
**Jared Freeze** 20:30 I think even this doesn't really get into it.
It just says, go to the homepage.
No, that's fine.
**Cleo Schneider** 20:41 Okay. Cool. So I will… I will update that doc. I'll remove the link to… to Node. I'll document that we should be pointing folks at the .NVMRC. I'll make a comment that that is… the NPM part is the important part, that Node should… you can use you should be able to use other versions of Node, and yeah, we'll go from there.
**Jared Freeze** 21:08 I don't know if anyone's using NUB yet, but it's like an abstraction layer on top of NPM.
If we use the linked strategy, which is experimental, we've been using it in other repos, and it works really well. It's super fast, it keeps a store inside the node modules folder.
That's pretty slick. You do have to change the way the repos… in monorepos a little bit, so I'll explore that too, because I think that that tool is, like, NVM and Node.
and NPM, like, all… like, it just works. Like, it reads Package Manager, it reads NVMRC, and just… if you do nub install, it just installs everything and just runs. So, that may be some… it's super new, but I don't know if anyone else has used it, but I was finding it pretty useful.
**Cleo Schneider** 21:57 I mean, that sounds sweet.
Okay, cool. That's… that's all I've got. Thank you, everybody.
**Jared Freeze** 22:06 Yeah, thanks.
Let's see, Wak.
**Joaquín Díaz** 22:10 Yeah, so I was reviewing David's PR about, the XHR instrumentation, thanks, David, for doing that.
And I found that, both in the new one and the old one, we do some… we open the spam when you call… XHR, open.
Which is not when you actually made the request. But in the old instrumentation, we used to have Span events, so we had a span event for Open, and a span event for SENT.
So it was easier to see when we actually sent a request or not.
But now that we are moving away from span events, we will have a small gap between open and send, where the request is not made.
Like, that's, like, that is client-side time, it's not actual, like, networking or anything that will add to the… what you actually want to know about the network span, which is how much time it took.
So I'm wondering if that is something we want to change now, or do we want to keep span events so anyone can like, understand when their requests are actually sent using XHR.
Or what approach you want to take there.
**David Luna Bistuer** 23:37 I don't know the solution, but I would prefer to avoid spam events, or at least use the API.
**Joaquín Díaz** 23:44 Yeah.
Would it make sense to open this band?
I wouldn't say open, so it's not confusing. Would it make sense to start the span on send instead of open?
And we just, like… we will have to, I guess… saving memory while we add on span on open, because on open we have the URL and the method, and then once you send, we'll have to match those somehow. I guess we already saved this one, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:19 I think it actually, like, as far as, like, measuring, like, what actually happens, I think it does make sense, in my opinion, to… to start the span on sand.
But… There may be some… some edge cases where, like, if you… That we should take into consideration, like… For example, like, if you, if you create the XHR object, and… Did you defer sending it until later, like, in some… You know, maybe, And it runs in a different context, then, like, the parenting could, like, be different from when… from when you call open and from when you call send?
**Jared Freeze** 25:06 I mean, we could… Totally different idea, but you could insert a timestamp, like, you could have a timestamp here.
And then… put the whole thing in a try.
Throw with a log.
And then start the span here with the previous timestamp.
I don't know if that's a good idea.
**Joaquín Díaz** 25:31 I think we do want timestamps to be when you call send, because that is when you actually start the network request.
I don't know if you can change the stadium of a spam after the fact you created it.
That will solve the issue about parenting, like, if you have a context when you call open.
Then, in there, you create a spawn, then you change the start time on send.
That would probably fix that case, but I don't know if it is slow or not, or if it even makes sense or not.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:12 Yeah, I mean, I don't… I… that's probably, like, a very… Rare-use edge case, I don't know if it's… worth, like.
**Joaquín Díaz** 26:18 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:19 solving for, but I… I do agree that that the send is probably the actual start we care about, so…
**David Luna Bistuer** 26:29 Well, that would, there is another case, I think that's where there was a comment from, from Joaquin about this, is if you are… you can reuse descent, so you can have a… an XHR object, and then you can just send, and then after a while, send again.
So maybe, I don't know, maybe you're doing some kind of polling, and then you just have one instance of the object, and then you're, from time to time, you're just applying calling send.
Having the creation of the span on the sand would… Also cover the use case.
If not, we should do them… I don't know.
Could be. We should do something different to… So at least to cover that use case on multiple sends.
**Joaquín Díaz** 27:18 Yeah, I mean, if you call send multiple times, then you start multiple spawns, but you will also get multiple callbacks when the request ends, that ends at spawn.
**David Luna Bistuer** 27:30 Yeah, yeah, no.
**Joaquín Díaz** 27:31 So I think it's fine.
Yeah, I don't know if we have to worry too much about that case. I think it's more important to track the time correctly for most cases, which is open and send and ending on wherever callback gets called.
And then, yeah, if there are cases where it's wrong, It's… I think we should document that, that… we expect… send to equal once, or open to equal once. Otherwise, it may… you may create multiple spawns, or they may be wrong time-wise.
But I think… I wouldn't try to make it more complicated, so we cover the 2% of cases that are weird. I think if we just have simple code for 98% of the cases, then it's fine.
**Jared Freeze** 28:26 Yeah, the only question I have is, you know, if you want to know how long something took, not just the network, I think you want this included.
But, yeah, we can look at…
**Joaquín Díaz** 28:39 Yeah, I mean… you may want to know that, but I think that's a different use case. Like, in here we are… This is the network response, so we want to take the time machine we want to observe is how much time it takes.
to the actual networks, but if you have If you're doing something else between open and send, I think it's up to the user to create a different spawn, or whatever.
**Jared Freeze** 29:04 Yeah, that's fair.
**Joaquín Díaz** 29:05 Am I fair that.
**Jared Freeze** 29:06 Yeah.
**David Luna Bistuer** 29:12 Can we conclude that we are… Can we conclude that we are going to use the… to serve this panda when sand is cold?
**Jared Freeze** 29:21 Yeah, I think so. Sounds like it.
**David Luna Bistuer** 29:23 Okay.
Okay.
**Joaquín Díaz** 29:25 And we don't want to keep spiny notes.
**David Luna Bistuer** 29:31 I love that. Thank you.
**Joaquín Díaz** 29:33 Thanks.
**Jared Freeze** 29:35 Cool. Wolfgang.
**Wolfgang Therrien** 29:36 Yep, this one's just quick, I saw that the web vitals, now support soft navigations, and wasn't sure if, I didn't see support for it in, our instrumentation there, I think it might just require some, like, opening up some configuration for it. So, just trying to get a gut check on, like.
Is it worth the… that juice worth the squeeze right now?
happy to open up an issue and a PR, but if folks are like.
No, we don't need that, but I will do it.
**Joaquín Díaz** 30:14 I think it's good to have it, but it's also good to call out that this is only for, like, newest… newest Chrome, like, really, today's Chrome.
But yeah, I don't think it hurts, I mean…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 30:33 Is that feature in Chrome experimental, or is it,
**Jared Freeze** 30:40 It's stable.
**Joaquín Díaz** 30:41 today.
**Wolfgang Therrien** 30:41 Yeah, I thought it just… I thought it landed unstable recently.
**Jared Freeze** 30:47 I think it was last week.
**Wolfgang Therrien** 30:49 Yeah, it was pretty recent.
Alright, I'll pull on that thread a little bit.
**Jared Freeze** 30:58 Cool.
Anybody else? I mean, I know we're at time, but… Okay, awesome. We'll see everybody next week.
**David Luna Bistuer** 31:12 You know?
