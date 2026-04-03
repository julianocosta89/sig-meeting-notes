SIG: Browser SIG
Date: 2026-04-02
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/VlkP3Sk7NZixiZW9AdEVeKgpHWbIpp14w8GkHfOHYeYpC3q9wYcIDVXFa3epXUSj.JL-BRL36L8Nw1ofw
============================================================

## Zoom Recording Transcript

**Jared Freeze** 00:27 Hi, Hector. Thanks for coming.
**Hector Hernandez** 00:31 Hello.
**Martin Kuba** 00:35 Right there.
**Jared Freeze** 00:37 What's up?
**Martin Kuba** 00:40 Busy.
All of us.
**Jared Freeze** 00:45 It got insane, like, the last two weeks has been completely out of control, I'm not sure.
It's in the air.
**Martin Kuba** 00:52 Yeah.
**Maxime Quentin** 01:03 Hello?
**Jared Freeze** 01:05 Hey.
**Martin Kuba** 01:06 Hi, Maxine.
**Jared Freeze** 02:14 Can I ask what team you're on, Hector?
**Hector Hernandez** 02:19 Sorry?
I was…
**Jared Freeze** 02:21 I'm curious what team you're on at your job.
**Hector Hernandez** 02:24 I'm, I work in Microsoft in Application Insights and Azure Monitor SDKs for, JavaScript, that includes browser, Node.js, and Python.
**Jared Freeze** 02:35 Okay, cool.
**Hector Hernandez** 02:36 Yeah, so… Browser, definitely heavily been used in Microsoft, so we do care a lot about it.
**Jared Freeze** 02:44 Nice.
**Martin Kuba** 02:45 Hector, do you work with Nev, by chance?
**Hector Hernandez** 02:48 Yeah, yeah, yeah. We work together.
**Martin Kuba** 02:51 He's, he's too… be part of this group.
Alright, I think we can probably get started, I only have, just two things, request for review. The first one is an update to… to our README with, based on… The… The release that we had, so we now have… We have, instrumentations that have been released, so I've just updated the README with, example that… That represents, what we have more accurately.
And then this, the previous example had… the… kind of the legacy instrumentations, like the Fetch and XHR.
And I did move those to a separate example, so I added… I'm adding an example with tracing.
That combines the event-based and… spam-based instrumentations in this example. But the README, I'm just… I'm just listing what we have in this repo.
So that's, that's one.
And the other one… is, We've been working on this resource timing, instrumentation for a while.
And I think… I think it's very close to… to being done, so I'm, this is a request for review.
I think the only thing that's pending, and we'll talk to Hector about this, is the semantic conventions.
I would… I'm… I would like to merge this with what we have right now, which is… which is, Basically, just a placeholder semantic conventions, and then, based on what we decide, we can open a separate PR to update the semantic conventions here. But if you disagree with that approach, let me know, but I think that would be okay.
**Jared Freeze** 05:40 I'm okay with that. I think, that's what experimental is for, what it means, so totally cool.
I would bias towards merging than not, so… It's my two cents.
**Martin Kuba** 05:56 Yeah, just… just in case, especially, like, if the… if the… If it takes a while, like, to… to land on… Or make a decision on the semantic conventions, then we're not holding this back.
Any questions or comments on this?
**Jared Freeze** 06:17 Let me give them a look.
**Martin Kuba** 06:19 Cool, thank you.
Okay, Hector, you wanna talk about… let's talk about the semantic conventions, then.
**Hector Hernandez** 06:25 Yeah, yeah, thanks, thanks, everyone, for reviewing this PR. This PR has been there for… It's getting very old. This was a continuation of something that Carly started a while ago.
I will… well, the thing here is that when I saw this PR, it's like, oh, this is pretty straightforward. It maps to whatever the W3C says, so W3C people already spent months working on this. We can just… we're not redesigning the wheel. The wheel already exists, right? So… but, Looks like with the unification, for client, this is causing some noise here, some, confusion, but at the end of the day, I just want to clarify, right?
if this is confusing to the customer, most likely we will absorb this confusion, because we will just grab wherever OpenTelemetry field is there, and we will transform it into some Application Insights or Azure Monitor field, right? But even so.
internally, people could be just debugging, could be just looking at the code, could be trying to understand what OpenTelemetry does, and then come to these properties, and they're like, well, what's going on? So… My concern is more about… the reasoning why we're doing this is like, it doesn't make… it doesn't feel like we're gaining anything from it, right? It's just causing more trouble, so… it's like you have a car and a motorcycle, both have wheels, both have engines, but you don't have, like, a diagram for… you just don't put it together, right? What's the deal of just having two semantic conventions different?
In there. That's… that's the part I… I just don't get.
**Jared Freeze** 08:18 So I definitely have a different take on it this week. I'm actually working on this separately, like, just… we've been going over it because we have a large mobile team.
And… I wanted to introduce HTTP.connection.
but not to map exactly to what the keys are. So start and end, I think, have their uses, but I think durations make way more sense, like actually working out like, doing the math, right, for the customer, because I think… If you're gonna go with logs, having a duration that you don't have to compute yourself, I thought would be really useful.
If the SDK did that, and then you had a key that represents it. So, that's kind of what I was leaning towards. Like, connect start time as a timestamp.
Okay, like, I can plot that, I guess, but if I want to see how long the connection takes, or I want to do metrics on it, like, it removes that arithmetic, like, one extra step.
I don't know if that's… useful, or if everyone agrees, but I was finding that, that was a raw value that I think more people sort of asked for than start and end. And working out, too, like.
You know, having a key called, like, other, which is all the stalled times that are not reported. So you have, like, the full, like, HTTP lifecycle.
But then there's a bunch of places where it will pause that it doesn't do anything. So, like, having a duration for that's cool, because you don't have start and stop times. So, having, like, just durations was something I was leaning towards. Not to say we can't just add all these keys, right? So, http.connection or DNS or whatever, but, you know, maybe, Doing the math.
Is better for… But, like, regular users?
That was kind of an added idea, but not doing browser.anything.
You know, because it's not really browser-specific.
like, resources are shared across anything with an HTTP lifecycle, so…
**Martin Kuba** 10:23 Yeah, no, so I think there are two, two kind of separate questions. One is, one is, Do we want to use… do we want to capture those? Sounds like… Jared, like, do we want to capture… The data as we get them.
Just like the timestamps? Or do we want to capture durations, calculate durations?
And the… if we'd go with the first one, then the question would be, do we… do we want to have… Some other conventions, there are… Something like this, like browser-specific, resource timing.
Like, browse Resource Timing, and then, like, the actual name of the field.
Or work together with, with, With the mobile folks on… and others, like… To reuse existing attributes.
From the HTT.
**Jared Freeze** 11:16 I mean… The reason I like the reuse idea is because you can use timestamp and observe timestamp to give the start value.
And then if you have the duration, you can… you know exactly how to plot that thing.
Right? And I think it makes it easier for logs, because you no longer have span events with, like, beginning and end, or whatever. I think it just lessens the number of keys you need, because, again, you already have timestamp.
So, that was kind of my thought. It was like, how do we have less data? Because I do think we have a different… responsibility than Node, which is, like, try to make the network requests smaller. I know that, like, a lot of backends don't really care about that. I think we do quite a lot, so… that was… that was kind of the idea, right? Because I think that does kind of drive, like, a lot of the things we're doing, right? So we were talking about how… you know, trace is fairly large, and logs is large, and all these things, so how do we sort of get the bundle size smaller, but then also have the network sizes be smaller as well, and I thought that was an easy way to do it.
Because not everyone's gonna use compression.
**Martin Kuba** 12:28 Yeah.
Yeah, I mean, I think it's this… I think this, from our perspective, this also kind of… Touches on, like, if you should have… should have, like, a philosophy of… Of just capturing the data as we see them in the browser.
And reporting what we see, and let the backend do the analysis.
Or if you want to do some pre-processing in on the client.
**Jared Freeze** 13:00 Definitely takes more cycles. I mean, there's CPU, like, committed to this math, so that is… that is different.
I don't know if everybody's gonna want that.
But that really doesn't have anything to do with the key, right?
Yeah, I mean, you could have both. So, yeah, maybe we just make it more flexible and have both?
Just have all the keys, and include durations as well.
I don't know.
If that's, used in other places.
Or you have both, like, start, end, and duration.
**Martin Kuba** 13:34 Yeah, I… I think I've… I think if… at some point, like, I've seen people do calculate iterations, So I don't think it's… I think it makes… makes… it does make sense.
But if you wanted to… if you wanted… if you did want to send the… the timestamps.
I guess the question is, we need to make a… Do we have… can we… Do we have, as a group here, like, from the browser perspective, do we have… a strong… Opinion one way or the other.
I can sort of see, like, I can sort of see, like, from, like, the semantic conventions, someone who's managing, like, the whole semantic conventions registry, that reusing existing attributes makes sense.
Having that consistent across.
At the same time, like, if I was a browser, developer? Or web developer?
It would be… it would definitely add some… some… Some cognitive overload for me, like, to… now that I have to map the… Like, which of these names actually corresponds to… the ones from the resource timing API that I'm familiar with.
So it's, like, two competing… Perspectives, I guess.
**Hector Hernandez** 15:14 Yeah, I'm obviously on just having the browser one only. We don't… As far as I know, we don't even have SDK for mobile devices, so this is not a business need for Microsoft, at least right now, so… We add the extra complexity, it's like, oh, yeah, yeah, but who are we actually benefit here?
Is it possible to have, like, a shared… share the schema between, like, a subset, right? That's another thing I realized, is like, okay, we have a unified, it's just not applicable to browser, a lot of things. Can we just have, like.
then 3 definitions, the browser, the client one, and the one that converged, even if you have these names, we can have some kind of, this is the kind of type, the definition, what it is, something like that. I don't know if Semantic Conventions has done something similar in the past.
Some middle ground, that's what I'm looking for, right?
**Martin Kuba** 16:20 So, sorry, what would that look like, the middle ground?
**Hector Hernandez** 16:23 I'm just bringing ideas, I'm not sure, right?
**Martin Kuba** 16:27 Okay.
Yeah, So, let me… let me put this… put it this way, I mean, for the folks here.
Like, if, if, if, like.
like, if he did decide on the unified Semitic conventions.
if the direction was set for us, to go with the unified Somali Conventions, would be, like, would be… Would it… would be, like, Feel like it's the wrong thing, like, from your experience.
**Jared Freeze** 17:11 I mean, I would say no. I mean, there's a request, there's a connection, and there's a response.
Right? Like, that is how HTTP works. It is for everybody all the time. It's the same thing. It is client, but it's, you know, sort of known. I'm not sure the names for resource timing, like, yes, they are useful, but… you know, having a standard, I have no problem obscuring this, honestly, because I think they should be intuitive.
Not to say that W3C doesn't do amazing work, and they picked good names. They did, but I think for… you know, for clients, I… I think it should be unified, but again, I'm biased, right, because we have a lot of mobile. So, that, you know, I mean, that's what… when you say the word standard, I mean, that's what it feels like, right? Like, you have to make that compromise. I am okay with that. My vote is shared, not prefix browser, I think. That's kind of where we settled. And again, the second key, my only feedback here would be instead of having, like, Secure Connect be the second key, I would commit to just… Request connection response.
I think that's what I would put forward here. And then, if we would want to just tack on the keys as they… as they exist for the W3C, Or, or, you know, whatever, it's on MDN, we can… Like, evaluate it like that, instead of breaking them up here.
Right? Where they're sort of period delimited, and they're even different. They're different than sort of both.
The current client and, you know, what's on, in the spec itself, so… Like, I don't really know about worker here. I mean, have to think about that one, but…
**Martin Kuba** 19:02 Yeah.
I mean, clearly, like, there are some that are missing.
I think we have… Yeah, I have, yeah. There are a few, few other ones that we have to… they're complex… that we would have to define… Separately?
Yeah.
So it makes it look… Adds, like, another layer of complication.
Alright, so to move forward, I wonder, like, if we… if it would help to… open, like, get that, that instrumentation merged, and then… see… see… actually… actually, like, add these in and see if they would actually work, because I think right now it's… Like, actually see it in concrete, concretely, like, in the instrumentation.
Maybe, like, we'll find that it's not gonna work well.
**Jared Freeze** 20:18 Would you want to branch the code?
Like, have a config option that's, like.
**Martin Kuba** 20:23 browser now.
**Jared Freeze** 20:23 namespace, HTTP namespace, and, like, let people test it out, so that way it's not just all reporting all these keys.
Or do you… does anyone care? Should we just report them all, and just report back in a couple weeks, you know, if somebody's able to deploy it?
**Martin Kuba** 20:41 Right.
Yeah.
We can, we can have, we can discuss it on that, on that PR.
**Jared Freeze** 20:50 Okay, that's fine with me.
**Martin Kuba** 20:52 And, I mean, the other thing that we could also do is, is take this to the semantic convention SIG, and get their perspective on this. They're probably gonna lean towards Unified.
And they'll probably say, like, what is our recommendation as RSIG? So… But, you know, we could probably get some feedback from them, too.
I won't be able to do it next week, I'm out of town next week, but I can… I can reach out, I can go to the SIG on the week after.
**Jared Freeze** 21:29 Cool.
**Martin Kuba** 21:30 Anyway, I think the next steps, at least for now, open a PR with this, with these unified, see, like, if it… how it actually looks, and if, I don't know, test it out.
See it more concretely. And then, Take it… take it to the… to the semantic convention sig.
**Maxime Quentin** 21:54 Do you have…
**Martin Kuba** 21:55 What do you think, Hector?
**Hector Hernandez** 21:57 I think Maxim have his… his hand raised.
**Martin Kuba** 22:00 Yeah, go ahead, Maxim.
**Maxime Quentin** 22:01 Yeah, sorry, very quick, like, could we just start with instrumenting both, like, both our resource timings, and, like, share the semantic timings?
And then iterate. Like, at least we are backward compatible, and if we see at one point that most of the boiler timing does not match, or are too complex to map to the shared semantic, maybe we can roll back to one or the other.
I mean, it's not like a… doesn't look like too many, fields, or having… having both of them.
could be a first step.
**Martin Kuba** 22:40 Yeah.
So you're saying start with the unified semantic conventions and see how it works, and go from there?
**Maxime Quentin** 22:49 Like, yeah, or even start with both, like, you know, you introduce both, and kind of collect feedback about how people use one or the other, if they feel like it's too complex to leverage proposed semantic attributes, or if they're really happy with the browser timings.
And iterate like this.
Rather than not having a full agreement first, and .
**Martin Kuba** 23:18 Hmm.
So have, like what Jared said, have it configurable?
**Maxime Quentin** 23:26 Yeah.
**Martin Kuba** 23:29 Okay.
We're gonna give it a try, see how it goes.
**Hector Hernandez** 23:36 Yeah, for semantic conventions, PR, I think Yeah, that's fine, let's continue working on this, right? We don't need to decide it right now, let's… I need to brainstorm, I need to bring this to the internal team to see what they think about this.
let's, if we can get semantic conventions people, feedback as well will be great, and whatever we decide, well, we will move forward with it, right? It's, It's not the end of the world, but yeah.
Yeah, let's try to do the right thing here. Yeah, I think it makes perfect sense, what you suggest, Martin. Let's give it a try, and… See how it looks.
**Martin Kuba** 24:12 Yeah, sounds good. Let's make sure that it doesn't get, stalled again, so… All right, got 5 minutes, Maxim…
**Maxime Quentin** 24:26 Yeah, like, very quickly, I, kind of migrated my, first, POC in the, OpenTelementary browser. So I created a sandbox, sub, workspace, And added a couple of files, plus, like, a deploy sandbox if we want to have it as a GitHub page.
Mmm… I picked, like, a small CSS framework and React to have some kind of basic web app.
And, did a first draft, so feel free to have a look and see, I really like it on that.
Only constraint I had was, like, Having all these changes made a quite huge package log change, so the… better review it per commit, so you don't have the, like, 2,000 line of change in the package log JSON.
But yeah, that's pretty much it.
No senior, but… First draft, so if you have any suggestions to make it easier to review, like.
simplify the code or whatever. But, yeah, merching machines.
That's what we've got.
**Jared Freeze** 25:54 So, I do have feedback I'll leave on the PR, but I really think this should not be in the workspace.
Having a dev dependency on React in, like, the route, I… don't love. I actually really like that you did it all in HTML, and then in your last commit, you converted the whole thing to React. I thought it was pretty slick before. But… my… I feel very strongly that we should not be sucking, you know, all these other tools into it, because React just has so many versions, and so many people are gonna, you know, be pulling it down. It's like, I don't want to do 500 packages for people that just want to run the demo. Like, I really do think it should just be a separate… Like, outside the monorepo, which I believe is how examples in core repo work, which I really like. So closer to, like, a bundler test.
That's my main feedback. I already checked it once, it looks good.
I prefer HTML, but I'm not gonna die on that hill.
**Maxime Quentin** 26:53 I mean, I'm pretty happy with HTML, too. I was just like, maybe it's too, like, too much CSS, too much, like, like, boilerplate to read, but at the end of the day, Exchange is still a bit big with the React and CSS library, so I can re… go back to the HTML session I had at the beginning.
**Jared Freeze** 27:19 Yeah, I'll take a look again. I mean, I don't think it's a big deal. You already did the work, and I think most of the world is building on React anyways, so… If it's what, you know, whatever's kind of easiest to copy and paste, because I think one of the other mandates that we have is, how do we get people to adopt more quickly? I don't want to have any extra friction, so… But yeah, the workspace thing is really the only major thing I would comment, but like I said, I'll give you a proper review as well.
**Maxime Quentin** 27:44 Thank you very much.
**Martin Kuba** 27:52 Alright, we're pretty much at time. There's a couple more minutes. Any other questions or topics, comments?
**Hector Hernandez** 28:02 I include the… for the console stuff, but we can just chat offline. It doesn't need to be in this meeting, right? It's just about the name that we want to use in the Node.js package.
Just to make sure that this never conflicts with the web one. Apparently, browser is going to create, like, a single package with everything? Is that what… what I understood correctly?
Okay, so maybe we can just use console without node, and it will be fine. There will be no confusion, I suppose. Okay.
**Martin Kuba** 28:37 But we still have, we still have, like, the name of the instrumentation, like, the scope, that should be different, I think.
**Hector Hernandez** 28:46 Yeah, my understanding is that both instrumentations will be different, will be creating different things, right?
**Martin Kuba** 28:50 Yeah.
**Hector Hernandez** 28:51 No.
**Martin Kuba** 28:52 Yeah.
**Jared Freeze** 28:52 Like, ours intrinsically has the word browser in it, right? Because that's our first subpart.
like, yours is gonna be instrumentation-console, and, like, it'll be at hotel slash instrumentation dash console. Like I said in my comment, like, as long as the README is very clear, like.
this is not recommended for the web, you know, this has the word require in it, or whatever. People will find out pretty quick, but, you know, as long as it's documented, I think that's good enough.
**Hector Hernandez** 29:18 Thank you.
**Martin Kuba** 29:21 Alright, I think that's all. Thanks, everyone.
**Maxime Quentin** 29:26 Secure?
**Martin Kuba** 29:26 Have a great day. Thank you.
**Maxime Quentin** 29:28 Bye.
