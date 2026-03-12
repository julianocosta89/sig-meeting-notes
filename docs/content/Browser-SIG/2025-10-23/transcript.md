SIG: Browser SIG
Date: 2025-10-23
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 00:43 You lose, you lose.
**Wolfgang Therrien** 00:48 Good morning.
**Ted Young** 00:49 Seems like my audio is not working.
**Jared Freeze (embrace)** 01:00 Hey, everybody.
**Wolfgang Therrien** 01:02 Hey, Jared.
**Ted Young** 01:06 Hmm…
**Wolfgang Therrien** 01:17 We can hear you, Ted. Can you not hear us?
**Daniel Dyla (Dynatrace)** 01:23 Ted cannot hear us.
**Wolfgang Therrien** 01:25 Okay.
Wasn't sure which direction the audio issue was in.
**Ted Young** 02:36 Alright, that's better.
**Jared Freeze (embrace)** 02:41 Welcome back.
**Ted Young** 02:43 How y'all doing?
**Jared Freeze (embrace)** 02:47 Good.
**Ted Young** 04:01 Whoa.
So… Just having a look. We've got a bunch of issues.
And, just some, like, general housekeeping.
Kind of, like, taking a break from this for a bit, because I was at first, a conference, and then an off-site for a week, and coming back, and it's like, we've got a bunch of issues, I tried… Hooking the project board up to a repo, so you can at least see the project board there now.
But I realized it's, like, most of the stuff we do on the project board doesn't… get reflected when you're looking at the issue view very well. For example, like, we can mark things as, like, available or ready for people to work on on the project board, and then that… you have to actually be, like, in the issue, looking at it to see it. It doesn't show up in the list view.
So, that's making me feel like… Our project board and its, like, current Configuration isn't as… As useful as it could be.
So, I'd like to just take a shot at maybe… Rather than using, like, project board-specific features, just doing everything with labels, because labels, at least, will show up everywhere.
And I think that will make things a little more sane, and then we can try to figure out which project board features work with labels.
Because all the stuff that's, like, project board specific doesn't show up in the issue page, so… I don't know.
I feel like that's the place people will probably be coming to first when they… they first show up.
Better project.
So… Those are just my feels coming back to the project after a couple weeks. It's like, this project board… Could be better.
**Jared Freeze (embrace)** 05:55 I like that idea, too, because I had, sent Martin a bunch of links for things that belong in browser, and I immediately wanted to see instrumentation labels, just to, like, get through it, because I was not… I was looking for not instrumentation topics. So, yeah.
**Ted Young** 06:12 Yeah, like, the search. I want to… things that are instrumentation and available, like, or whatever, right? Be a lot easier. The search feature would… So… Cool.
So, that said, yeah, the project board, not super useful to look at today, perhaps.
But if there's issues people want to talk about, maybe add them to the meeting agenda.
Rather than try to go through all 24 open issues, since we've only got, like, 20 minutes.
**Jared Freeze (embrace)** 06:57 Cool. I can get started, if you want to do that? Cool. Okay, so, as far as the environment goes, I added… there's a PR up for adding commit lint. It's basically just… adding the library, it's a one-liner. It is not modified. The maximum number of characters by default is 150, I saw that, hotel is set to 72. I just left it out, I figured just defaults are good enough. If we have a problem, we can change it.
And then I experimented yesterday with TurboPack, versus NX. I think TurboPack is lighter. The main difference that I cared about was the fact that NX lets you do that interesting thing where you can have a single command at root, and it will run it in the context of the package, so you don't need package, commands? Like, you don't need a build command.
I think, based on the overhead of NX, I don't really care about that, because I can't imagine we're gonna have as many packages as cantrib, and if we ever do, that's fine, we can do a code mod later, but having, like, a build command in each package, like, seems fine at this point.
It'll just be, like, Vite, or ESBuild. Fine, whatever.
So, that is not quite, it's a branch, but not a PR. I'm not gonna do that until it's ready already.
And also, I created a generator with Turbo, which is why I sort of liked, you know.
Yeah, right. Yeah, so, I made a generator for instrumentation. It works pretty well. I was happy with it. You know, I don't think we need anything that NX has that Turbo Pack doesn't, so that'll be my proposal.
Yeah, so I will post that when I can. The CommitLent PR is up if somebody could take a look. Like I said, it's a one-liner, but we'll chip away at this, you know, as we go.
**Ted Young** 08:59 Nice.
**Benoît Zugmeyer** 09:00 Is it a commit hook?
**Jared Freeze (embrace)** 09:04 Yes, I also added left hook, to make sure that lint runs, as well, so they're paired together because, you know, without it, you're not actually commit linting, so… But I included the biome command as well.
**Ted Young** 09:27 Cool.
Any thoughts? Anyone volunteer to do a review?
**Wolfgang Therrien** 09:36 Yeah, I can take a look.
**Benoît Zugmeyer** 09:39 Can we maybe include it in a workflow? I don't know if… If it makes sense to link commits in a workflow, but I'm using jiu-jitsu, and there is no hooks. So, yeah.
**Jared Freeze (embrace)** 09:58 I definitely… yeah, I mean, we need an issue for that to bring over pretty much everything from OTLJS and see what we need and what we don't need, because we want to follow a lot of the… you know, there's a lot of good stuff there that we… should review. But again, another issue, another PR, trying to keep stuff small at this point. But yeah, definitely, definitely one NCI.
**Benoît Zugmeyer** 10:21 Okay.
**Wolfgang Therrien** 10:24 Was the ask, to have it in a workflow… And not in a commit hook, or…
**Benoît Zugmeyer** 10:33 We can do both, I guess.
**Wolfgang Therrien** 10:34 Okay.
**Ted Young** 10:40 Nice.
Okay?
Next up, Joaquin, you've got some questions around semantic conventions.
**Joaquín Díaz** 10:50 Yeah, that'd be arduous.
been up very well. I don't know if… what else we need to do to merge it, because I'm working on the instrumentation for that.
And I think the best will be that that is merged before I finished.
I see a couple of comments, I can take care of them. I had a question about, like.
meaning, like, for example, I see a comment here that says.
Line 72, this is… this should be an attribute. I am not sure what do they mean with that.
what should be an attribute? It looks like an attribute to me, so I feel like I'm missing on some of the definitions I use, or the semantic conversions that I'm not used to.
So if anyone can… help me with that, like, there is another similar comment of another say that… another line that says, this should also be an attribute, so I'm not sure what they mean with that.
**Ted Young** 11:50 Do you mind just posting, in the meeting notes, just posting links to the comments you're having trouble resolving? Yeah. And then we'll… We'll see if we can pile in on them.
**Joaquín Díaz** 12:04 Yeah, hold on.
So, that one… On this one And then this one. Again, I'm… I'm not familiar with the language, so I don't know what do you mean with attributes.
**Ted Young** 12:40 Martin?
**Martin Kuba** 12:43 Yeah, I mean, so this PR has been open for a while, it doesn't have any approvals right now, so I think folks will probably have to get back into it, like, to… You know.
like, to finish the review, but I would say, like, it probably shouldn't stop you from writing the instrumentation. I think the instrumentation would actually help with, I think, might help with… Finishing the semantic conventions.
**Joaquín Díaz** 13:07 Yeah, yeah, yeah, I'm working on the experimentation right now. I'll probably have a PR later today.
I'm using this as a base anyways, even though it's not merged, but I'm using the attributes it's fine here.
So I don't have to change the data.
**Ted Young** 13:23 Yeah. Oh yeah, I come…
**Joaquín Díaz** 13:25 Should I just add a comment here once I have a PR saying this is instrumentation for this?
Will that help?
**Ted Young** 13:33 Yes, it would. That would give people one more thing to have a look at. I'll have a look at these open comments as well, and see if I can get them resolved.
But I think maybe a broader question we can have with the semantic convention SIG is, I think we'd like to… to move faster with things being experimental for a while. It's not that we don't want to review from them, but, like.
You know, if… As is common with these things, it's like, it's usually, it's like, there's, like, an 80-20 rule of, like, 80%, everyone's like, yeah, that's fine, and then people want to nitpick some stuff at the edges, and maybe saying, like.
Let's just… Let's just go with something for now, and… and get in a feedback loop.
Yeah. They may not be… they may be wary of this, right? Because they don't like, experimental, semantic conventions getting out in the world, and people getting hooked on them, and then breaking people.
But I think we can make the argument that this is an intentional effort, you know, we're not gonna leave it.
Experimental for very long.
**Joaquín Díaz** 14:46 Yeah. Yeah, that would agree.
Thanks.
**Ted Young** 14:50 Yeah.
But yeah, if you hear pushback from them, that's why, though, is because we've had other stuff that stayed experimental for too long, and now.
**Joaquín Díaz** 15:02 I'm like, yeah.
**Ted Young** 15:02 Oh, we're just stuck with these decisions. So, you might have some people being like, no, no, no, we should just sort it out right now.
So, but that's the…
**Joaquín Díaz** 15:10 Yeah.
**Ted Young** 15:11 That feel is coming from.
**Joaquín Díaz** 15:13 And that makes sense to me, but I feel like… feel like these attributes make sense for most people, because I don't see comments on the attributes themselves. It's like… I just don't know what they mean when they say this should be an attribute. Like, when you have the body and the fields, those are not attributes the body feels.
**Ted Young** 15:31 Right. I think it's a question of whether something's in the body versus something is an attribute. This is… one of these areas where there's… it just feels like religion a little bit. Like… like, to some degree, OpenTelemetry in the log data model, we ended up with a body field, which is itself just nested dictionaries. And so now, it's like, is something… Attributes, or is something part of the body field?
is, like… a little bit open to interpretation. We keep trying to make hard and fast rules, and then finding domains where, like, those rules are forcing us to do something really annoying, which is, like, not the point of having the rules.
So… But a side effect is, like, this… Annoying debate will pop up around, like, should something be an attribute versus part of a body field?
**Joaquín Díaz** 16:27 Yeah.
So, when you say body field, it's the actual, like, body of PE… Yeah.
blog message. But then, When we have the… Evan Dane, which in this case is browser.user action. Is that also in the body, but that's a different field.
I thought that was the…
**Ted Young** 16:50 And then you're talking about the actual, like, protobuf fields, like name and… There's… there's also a name field in the protobuf.
For the name of the event, which is the semantic convention name, is what goes there.
Okay The other protobuf fields are things like, you know, timestamp and stuff like that.
But we won't be… we wouldn't be adding new fields to Protopuff. That's not… that's not something… We should be proposing.
**Joaquín Díaz** 17:27 Alright, so, based on that.
I would assume that everything should be an attribute, and then just the name should be in the body.
For this, like, that will… that is what makes sense to me, and that… based on the explanation.
Right.
**Ted Young** 17:42 Well, you would have… the name would be the name field on the protobuf.
And that would be the name of the semantic invention.
**Joaquín Díaz** 17:49 Yeah. I think that would be in the body.
**Ted Young** 17:51 I think the thing we were looking at putting in the body here in RSIG is when we're getting objects from the browser, and we're just trying to, like, splat them.
In and ship them, or some truncated version of them.
Rewriting everything in, like, dot notation, kind of flat attribute syntax.
That felt weird, but now we're allowed to have nested stuff in the attributes, so it's sort of like you have one option of, like.
Having a field that describes what this object is that you got from the browser, and you put it in as an attribute field.
The other place would be to put it in the body.
**Joaquín Díaz** 18:34 And, and I feel like…
**Ted Young** 18:37 The community's been kind of swinging back and forth there.
And we're sort of settling on, like, maybe we just do everything with attributes, and we don't touch the body at all.
I feel like that's kind of where we've landed, now that we have nested attributes allowed.
**Joaquín Díaz** 18:54 Yeah, yeah, I think that makes sense.
Okay.
**Martin Kuba** 18:58 Yeah, I feel like when this… Yeah. In fact, when this OPR was open, like, we were, like, working towards putting everything, all the fields in the body, and since then, the thinking has changed.
**Ted Young** 19:10 Yeah.
**Martin Kuba** 19:11 I think, no, my understanding is that now, like, the… the, The direction we should follow is, like, everything is an attribute.
Yeah, okay. Yeah, only, like, serialized things should go in the body, so… So I think with that, I think this PR needs to be probably updated. Maybe you can reach out to Carly to update it.
Yep.
**Joaquín Díaz** 19:35 Yeah, I think… I tried to ping her on Slack, but, like, there are a few of them. I don't know which one, which user she is.
But if she's not responsive, I can take care of that and move everything to the attributes.
**Ted Young** 19:50 Sweet. That'd be helpful.
Yeah.
Daniel?
**Daniel Dyla (Dynatrace)** 19:55 Yeah, I was just gonna say, I think related to that, there also needs to be guidance Around when to use… Complex attributes versus when to use flat attributes.
You know, it may not be for this group to decide, but… the way that I've been thinking about that is, essentially, if you're… if you get something from the browser that is itself a complex Like, structure, and you're just… jamming it in, this is what we got from the browser. I would say that that's a good use for a complex attribute, but if you're gonna do any sort of parsing and manipulating, I would then put that onto a flat attribute. Like, if you're like, I'm pulling out some specific value from it.
**Ted Young** 20:39 Yeah.
I would agree with that, and that's because it's a lot easier for backends… like, I think the nuance we're trying to go for is, like, as a backend, should you see this attribute as some kind of index? Or should you be wary of this thing as just being some high cardinality splat?
That's, like, descriptive data that's used for something else.
And to kind of say that if it's showing up as a simple attribute, it… it might be high cardinality, but it should be a good index.
And if it shows up as, like, a complex thing.
You should just assume that's data, or descriptive data, and you shouldn't try to… to do anything useful with it.
And the only side effect of that is we should avoid starting to model situations where we're expecting people to reach into Complex attributes to make indexes. If there's stuff where we're like, this is a super important index that we think you should use all the time.
As part of, like, the data modeling we want to do for the browser, maybe… we're pulling those things out and highlighting them as attributes, even if they also happen to be buried in some Blob of an object that we got back from the browser.
That's… Again, there's some nuance there.
But that's… that's the one thing to think about, is just, like, what's being used as identity, what's being used as an index, versus what's just data that's gonna be used Some other way.
**Wolfgang Therrien** 22:12 where… where might we want to document our thinking on that strategy, right? So if we have, like, folks who want to contribute, they're not in this conversation, like, where… Where should that go?
**Ted Young** 22:24 So, that is the one thing I put on the agenda, just down at the bottom. We have a browser observability model we'd like to get cooking. It's in a Google Doc right now. I haven't had a look at it in a bit. I'm not sure if anyone else has, but… We should reboot.
Reboot that thing and get it converted into a pull request as maybe the next step.
**Joaquín Díaz** 22:53 Yeah, so… there is some work that I did, that is a PR study merged into the repo, which has events only.
Okay. That is… that is linking all the current, like, semantic conventions and current instrumentation.
But yeah, ideally, there is some stuff missing from their… from that Google Doc.
Okay.
exception, network requests and everything like that. It's just… these are all mostly… well, I think I have exception now, actually. Right.
**Ted Young** 23:25 Okay.
**Joaquín Díaz** 23:25 Yeah, this is Samsung, at least.
**Ted Young** 23:28 But then, I'm just giving everyone a link to that as well. So, we've got a list of some of the events already.
So the next question is.
what more do we want to pull in? And I think we want to give people more of a model than just here's all the events and stuff like that. Like, I think we want to also… Have, like, some kind of descriptive pitch.
Like, like, people were just saying, like, when people come to, like, OTEL Browser, there should be some landing page where we kind of are describing what… what our goals are, which is not a thing we do so much in the other SIGs, but just because browser and ROM are such a big space, I think it would be helpful to be like, our goal is to provide like, these kinds of dashboards and this kind of error reporting at this stage, or whatever it is.
**Dan Gomez Blanco** 24:24 You mean… As opposed…
**Ted Young** 24:25 Sorry, go ahead.
**Dan Gomez Blanco** 24:26 You mean on the repo, like, in that, in the OpenTelemetry browser repo as, like, a doc section or something like that, and design docs?
Yeah. Within that report.
**Ted Young** 24:34 Yeah. Kind of like…
**Wolfgang Therrien** 24:36 doc slash overview, maybe, like, a strategy section, but like, hey, if you're adding new instrumentation, this is how you should think about attributes, and then, like, what we have implemented so far, that's where, like, we can get really into the details of, like, hey, these are the shapes of these events, this is how we manifest these strategies in these particular use cases.
**Ted Young** 24:53 Yeah, right, so if someone's like, OTO browser's terrible, I'm trying to do session replay with it, and it… and it's not working, right? Where it's like, well, we're not trying to give anyone session replay.
At this point, right? Like, that's not… that's, like, a non-goal right now. But what is, like, if someone were to, like, critique our model.
Right? Being like, we're trying to, like, these are the targets we're trying to hit, then maybe we could actually get good feedback from people and be like, well, actually, I need these other indices, because this is how I need to be able to segment these dashboards, or what have you.
**Dan Gomez Blanco** 25:29 And that makes sense, because, you know, Google Docs are easy, but not discoverable, right, compared to…
**Ted Young** 25:34 Yeah.
**Dan Gomez Blanco** 25:34 Love that lives in a repo.
**Ted Young** 25:36 Yeah, I think the other place we'll get feedback is, like, people are… I mean, we've got various vendors on the call, but end users as well, being like, I'm trying to feed… OTEL is this special property of, like, people are going to be trying to feed it into all these different tools, and they're going to be coming back and being like.
it's missing something, so I can't turn it into blah data and look at it in this this traditional browser tool. Like, browser tooling is more proprietary, it feels like, than… than other stuff, so maybe there isn't as much of that going on here. There aren't as many Jaegers in, like, the browser observability world, but… still, you know, we should expect some kind of feedback about, like, this data is a square peg, and I'm trying to put it in some round hole over here.
**Dan Gomez Blanco** 26:23 Justin, in going back to the… Complex attribute versus… Flat attribute, Is that something that we want to document in that Google Doc first, and, like, as a section of, like, as in how we think about it, right? We just basically explained, Ted.
**Ted Young** 26:42 Yeah, yeah, I think one section about… this is what we want to provide. We want to provide this level of dashboarding and alerting for browsers focused on… like… not framework instrumentation even, right? But just, like, how the browser itself works, and how navigation works, right? And then, like, being, like, we have a concept of a session, right? In order to bundle multiple pages together, right? So, some section around how we're… we're gonna model navigation.
And then it's like, once we're past that, then we can talk about… in general, data modeling practices, and then at the bottom, finally, like, here's just a list of all the stuff we've splatted into the semantic conventions so far.
**Dan Gomez Blanco** 27:29 Good.
**Ted Young** 27:30 So… .
**Joaquín Díaz** 27:32 Yeah, but I wouldn't use Google Docs. I think I will just create a.
**Dan Gomez Blanco** 27:36 I mean… Yeah.
**Ted Young** 27:37 Yeah.
Feel free to just start moving this into PRs at this point. Yeah, absolutely.
**Dan Gomez Blanco** 27:45 Yep.
**Ted Young** 27:49 Okay, and then I'm gonna go… we do have, like, a pile of instrumentation we'd love to get donated, or stuff to get written. I'm gonna refactor that stuff out of its current it's kind of buried a little bit in our project file. I'm gonna try to make that more obvious.
When we look at our issues page.
Okay, we've got one minute left. I think we… Jared, we skipped over bundler support?
**Jared Freeze (embrace)** 28:17 It was just a reminder, take a look. I put forward something super simple and modern.
Nice. You know, it's not legacy. I think that's where the world is at, and, you know, all these other nodes are EOL, so…
**Ted Young** 28:32 Great.
**Jared Freeze (embrace)** 28:33 Cool.
Everyone take a look.
**Ted Young** 28:35 Yeah, everyone, post updates to Slack as you're… you're making changes.
Live a little bit faster.
See you next week.
**Joaquín Díaz** 28:46 Bye.
