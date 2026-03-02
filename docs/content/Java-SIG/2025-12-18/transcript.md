SIG: Java SIG
Date: 2025-12-18
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg** 00:34 What's up, John?
**John Watson** 00:37 Good morning.
**Jack Berg** 00:50 Finally got this PR merged.
from Anurag, who was adding new internal telemetry.
Following the new semantic conventions that are experimental.
And, I felt so bad about it, because, Jonas had, you know, opened two PRs that were the same thing back in the summer, and, you know, we just kind of lost track of them. But, you know, at least all's well that ends well. We finally got it merged, and…
He'll work now.
**John Watson** 01:20 That's good, good, good. And we kept, if I recall, we kept the older metrics around.
**Jack Berg** 01:26 They're around, and they're the default, and so you have to explicitly opt into the new, format by, you know, setting… it's calling set internal telemetry version.
**John Watson** 01:37 Right. Yep.
**Jack Berg** 01:40 And I just opened a new issue to figure out how we can opt into that with declarative config, so that will sort of connect all the dots and make this something that is actually usable, because right now you can only do it with programmatic config, which nobody actually does, or very few people, I imagine, and hope.
Trask, are you still without power?
**Trask Stalnaker** 02:11 No, I have power!
But I have, my mic is not…
Going to the right place.
implement… implementation.
Interesting.
That's better.
**Jack Berg** 02:48 Yeah, there you go.
**Trask Stalnaker** 02:49 Yeah, have power.
How about you, John? Any, exciting wind…
**John Watson** 03:01 You know, all over the neighborhood, there's tons of branches down, but I think we slept through it, and we never lost power, and everything was fine at my house, so…
I don't… I was, like, going for a walk yesterday. I'm like, where do these branches come from? What's going on here?
I suppose I hear we're supposed to get more wind today.
Along with the rain.
**Trask Stalnaker** 03:24 But… Sucks.
Wind sucks.
**Jack Berg** 03:29 When we're talking winds, like, what kind of wind are we talking?
**John Watson** 03:33 I think gusts, like, up above 50.
50 miles an hour.
**Jack Berg** 03:37 Oof.
**Jay DeLuca** 03:38 I just got an email 20 minutes ago from my power company saying they're expecting 60 mph winds here tonight.
And it's real cold.
**Trask Stalnaker** 03:53 Luckily, it's not that cold here.
So, like, had no power yesterday, but… so…
Spent the day doing yard work.
**Jay DeLuca** 04:05 Nice.
**Jack Berg** 04:11 Yard work in the wind.
**Trask Stalnaker** 04:13 Was it windy during the day?
At least not here. It was not… it was kind of weird. Norm… yeah, it wasn't that,
didn't feel like it was that windy here, even that overnight. I was surprised that we lost power, but…
throughout the city, it was, I think, windier in other parts.
Alright, thank you.
All for coming to the last meeting of the year.
I threw a couple of declarative config topics on… To chat about…
I'm really torn on this, Jack. Yeah, I can see, like… at first I wanted to… so, okay, the question here is,
when we… access properties. So, in instrumentation, we want to, get an instrumentation property.
If that property exists in the YAML, but is not the type that we're expecting.
Do we want to return null ?
Like, as if it doesn't exist?
Or do we want to throw an exception?
And sort of say, hey, this is… Clearly, User intent was… Wrong.
And we should fail fast. So, the…
**Jack Berg** 06:03 both.
Maybe both, like, maybe give the ability to fail fast, or maybe give the ability to be more graceful, based on just, like, sort of preferences of whoever is writing the instrumentation, interpreting these things.
**Trask Stalnaker** 06:19 Fair. But what would we… what do we even want on the Java agent side?
is… initially, my thought was, oh, I definitely
don't want to fail fast, I want, you know, the Java agent to still come up.
And, you know, like, ask just to log a warning inside of, you know, the SDK if it is the wrong type, kind of a thing.
But then, thinking about it more, like, I mean…
I don't hate the idea of… the…
of failing fast, of, I mean, if the configuration is wrong, we're not gonna take down the app, but we will take down the Java agent.
**Jack Berg** 07:07 What do we do today for system properties and environment variables? Like, if we're trying to… I think…
if you're specifying an environment variable, obviously environment variables are always string… strings, but, like, let's say we have a Boolean one, like the…
hotel…
like, the Boolean to enable or disable the agent. And so we're going to try to parse that as true or false.
And, you know, if you put a string in there, like foo, what happens?
**Trask Stalnaker** 07:39 We great, we're… we do not fail fast.
**Jack Berg** 07:45 You just, you trudge on and install the Java agent?
Or, like.
**Trask Stalnaker** 07:51 We either detect, I forget what, but in all cases, we're going to… like, that's kind of a unique case, because it is whether to start up the Java agent, but all the other properties, we just pick a default.
**Lauri** 08:06 Maybe Boolean isn't, like, a good sample, because,
the standard parse boolean method, it just compares the value to true.
So anything else is treated as false.
But for numbers, I'd assume we somehow fail.
**Jack Berg** 08:23 Yeah, actually, I'm looking at the code for config properties.
Config properties is the, you know, the facade for accessing system properties and environment variables, and if I look at getInt, for example, you're trying to get an environment variable or system property, you know, as an integer.
We throw exceptions in there. So you're going to want to go to default config properties, that's the implementation. There you go.
**Trask Stalnaker** 08:53 We do, so…
**Jack Berg** 08:56 So that's, like, a fail fast.
**Trask Stalnaker** 08:57 Okay, okay.
So that's some good precedence.
I think I'm good with that, especially given the precedence, then.
I mean, Boolean is… gonna be a change, since, as Laurie said, it, we probably weren't.
Yeah, this isn't gonna throw an exception.
but will… In the game.
**Jack Berg** 09:43 the,
The other thing that I noted in that comment is even though the Java doc says today that we're gonna throw, if the type is wrong, the implementation doesn't.
So the warnings are fake. And so, you're…
You know, we'd have to make a code change to do this fail fast.
**Trask Stalnaker** 10:07 Yeah, the real question I guess I had was, yeah, if we…
would… I mean, if we do have the throws, do we try catch around that?
In all our instrumentation code.
But… This is convincing to me.
**Jack Berg** 10:29 Just quick question around the try-catch. So…
so I… I think, and maybe this is obvious, but, you know.
You'd want to… like, what should happen if…
An instrumentation is trying to load and install, and an exception is thrown in config.
And it's not gonna catch it. Does that instrumentation just not get installed?
Or does the whole Java agent not get installed?
**Trask Stalnaker** 11:04 I don't know the answer to that question.
**Lauri** 11:08 I don't know either, but
Like, it also kind of depends on when exactly the exception is thrown.
like, in the ancient, like, lots of the configuration is read in those singleton classes.
This is actually a class that's defined in the application… in the… in the application.
And, the instrumentation has already been run, so…
The end result will probably be that the static initialization of the singletons class fails.
And this will probably bring down the whole application.
**Trask Stalnaker** 11:49 That sucks.
**Lauri** 11:51 I would assume.
Because any time, like, the instrumentation tries to use the singleton class, it will get a new cluster found error because the initialization failed.
**Jack Berg** 12:05 So what…
So there's some things to think through with that, but I guess, like, what would be the ideal scenario?
like… I, you know, in my head, one scenario…
would be, if any instrumentation fails to install, the whole Java agent fails to install, but the application continues as normal.
But I don't know how practical that is. We'll always continue as normal.
What about what Lori was just talking about?
**Trask Stalnaker** 12:39 That… that scares me. That is… I agree with Lori, that… But the thing is that, like.
**Lauri** 12:47 If an application fails during startup, then,
It definitely isn't as bad as failing.
During runtime, at some random point.
**Trask Stalnaker** 13:02 So we either need to have a very careful pattern around loading in, instrumentation config… Or… we…
Would want to wrap everything All of those callers in… Try catch.
Or change the behavior, ask to change the behavior of the SDK.
**Lauri** 13:28 I think it probably isn't, like, a big issue in practice, because,
Most of the configuration properties are just strings or booleans.
And neither of them fail, with exceptions.
**Jack Berg** 13:41 Yeah, it's not very common to have, like, an int, is what you're saying, that would have a number format exception.
**Lauri** 13:49 I don't even know whether we have any, like, in the instrumentations. We def… I definitely don't remember any of any failures because of
Because of that.
**Trask Stalnaker** 14:04 do we… I mean, what is the declarative config say about Boolean properties… Is there any graceful…
Fallback there, or it's pretty strict.
**Jack Berg** 14:19 Well, so, booleans… for declarative config, it's, you know, we're delegating to YAML semantics.
Right, so you put in a YAML file, and you know, you have a key-value pair, and the YAML specification tells you how to parse the value in, like, resolve the node type.
And so, you know, whatever YAML says about,
Booleans is what declarative config is doing. And then, you know, by the time declarative config and we actually have a saya in it in Java, like, you know, the YAML parser has already resolved the node type, and, you know, it's either a Boolean or string, and we don't try to do anything additional.
**Trask Stalnaker** 15:04 Does… pardon my YAML ignorance, but is… do my… do strings always have to be quoted?
**Jack Berg** 15:12 No, no, so that it, like, if you, if you… if you double quote or single quote, there's a variety of ways to quote strings, but that, that, like, is doing a type coercion thing.
Where you're telling the YAML parser, hey, this is a string. But if you leave it unquoted, you're kind of, you're kind of leaving it to the parser to interpret the value, and there's all sorts of rules for how the value is resolved to a node type.
And, I guess the other thing that's important is, like, you know, if the value isn't being
coerced into the intended node type, maybe there's, like, ambiguity or something, there's this special syntax where you can, like, force the coercion. You can, like, tell the YAML parser explicitly, hey, interpret this as a Boolean, interpret this as a number.
**Trask Stalnaker** 16:03 And that's part of the YAML spec?
**Jack Berg** 16:05 Yeah.
**Trask Stalnaker** 16:13 So you… you can't, like, even have a straight, like, this would be parsed as a Boolean.
**Jack Berg** 16:20 Yep, that's parsed as a Boolean.
But you can, if you put double quoted it, then you can force it to be a string.
**Trask Stalnaker** 16:29 Yeah.
**Jack Berg** 16:34 So just, like, going back to this, like, hey, does the whole agent fail to install, or is it just, like, an instrumentation library? The thought that I wanted to convey with that is, like, hey.
I don't think we can say that if a single instrumentation library has a config
Type mismatch, that we can just, you know, prevent the whole agent
From installing, because aren't there going to be instrumentations that, like, install at runtime?
Like, is… are all the instrumentations installed Add application start, or no.
**Lauri** 17:11 Well… Did, like…
what we consider an application start is kind of vague. Like, you could have an application server that deploys a WAR file.
And Don deploys it, so it could happen at any time.
**Trask Stalnaker** 17:29 Also, even in the kind of happy path, if…
an instrumentation… I mean, we install all the instrumentations in some order, and if one of the later ones fails.
we've still already installed the bike code changes for the earlier ones, so you're kind of… not in a great state, I think.
**Jack Berg** 17:54 Yeah, so that kind of points me towards, like, you know, try to wrap the installation of any particular instrumentation library in some sort of try-catch.
Which, you know, if there is a configuration exception, it's just limited to that specific instrumentation module.
**Lauri** 18:13 Well, of course we could, like, redesign how…
our instrumentations are working, I guess.
like, with the new indie instrumentations, you could have, like,
You could read the configuration, when the instrumentation is, like,
When the instrumentation is, like, first discovered, like, when the agent starts, not the…
**Jack Berg** 18:41 Yeah.
**Lauri** 18:41 And, when the class is, like, defined in the application class loader already.
But currently doing that would be…
somewhat inconvenient for us, I think.
**Jack Berg** 18:53 Yeah, like, sort of decouple The interpretation of configuration
from the installation of the instrumentation. So, like, maybe you can interpret all the configuration at start, and by the time we try to go and install instrumentation, we know that all the configuration is correct and validated.
**Lauri** 19:16 Yeah, but we currently can't do it easily.
**Trask Stalnaker** 19:30 And how… okay, that… that helps me with stuff to think about for the,
For this, for the Java agent.
For library instrumentation, so, people out in the world.
**Jack Berg** 19:50 Yeah, library instrumentation. So, the typical pattern for library instrumentation is, like, you know, you're invoking the code to initialize it.
And, you know, typically you're setting your OpenTelemetry instance. That's what we ask, you know, users installing library instrumentation to do. And it may be in a builder or something like that, where you're building up some, you know, client or component that's going to be wrapped with OpenTelemetry.
And so, in my head, maybe at the time that you call, set open telemetry, or maybe, like, when you're constructing
your client or component that needs to actually install meters and tracers and do all that type of thing, set up your instruments, maybe that's when, you know, those library instrumentations would
would, you know.
**Trask Stalnaker** 20:40 Resolve the configuration.
**Jack Berg** 20:42 Yeah.
And so it's, you know, then… and fail if it's incorrect.
**Trask Stalnaker** 20:50 I'm… How does this, trying to think if this has any impact on dynamic configuration.
I mean, it's almost kind of nice to have that.
Resolved configuration object that then, like, dynamic configuration would come in and re-resolved.
That, again.
My only worry is that we're kind of, like, this is gonna be a pattern, that we have to…
Basically, tell everybody to follow this very specific pattern to get good behavior.
**Jack Berg** 21:29 Yeah, so…
I don't think… I think we can come up with our own opinions for how the Java agent instrumentation and our library instrumentation that we, is, like, under our purview, how it operates and the patterns it follows. So, if we want to say something like, hey, the Java agent instrumentation chooses to fail fast.
great. Like, you know, that's how we can do things. But, like, you know, it's gonna be really hard to be prescriptive to native instrumentations, especially, and tell them, like, hey, if there's a…
if there's a configuration type mismatch, you need to fail fast. I think there, you know, there's gonna be instances where people are like, no, we're gonna fail gracefully, because, you know, telemetry is secondary.
So, yeah, we probably want to minimally, like, give them the tools to fail gracefully, or something like that.
But I think we already do, because you can catch these exceptions.
**Trask Stalnaker** 22:30 So, back to, I mean… What if we don't throw… Exception.
What's the… kind of harm their log… log a warning.
inside of the SDK, if there's a type mismatch, and just don't throw.
**Jack Berg** 22:53 Yeah, yeah, so the,
Okay, so you're asking for a number, and, you know, the value is a string, we don't throw, and we return null , right? So your instrumentation gets initialized with the default behavior for whatever that is, instead of the,
Instead of…
**Trask Stalnaker** 23:16 The user intent. The user intent.
**Jack Berg** 23:18 And the signal to the user that, this… something is misconfigured according to their intent is, like you said, there's… we have these log statements within the SDK that say, like, hey, you know, for this property, the user, you know, asked for a number, but it was a string, so we return null .
And so, you know…
is the signal strong enough, essentially, to prevent confusion? That's… that's the question that we should be thinking about. Like, are those logs that we're emitting in the SDK, are they, you know, is everybody going to see them? One, and two, are they going to be actionable? Like, you know, are they going to have breadcrumbs to tell you where the property was in your YAML that was misinterpreted?
And right now, they don't. Right now, they're, like, really primitive, so they don't tell you… like, they tell you the property, but it's, like, just the local property key within that node. They don't tell you, like, the breadcrumbs of, like, the, you know, the parentage going back.
**Trask Stalnaker** 24:15 But that would be easy to capture the breadcrumb, right?
**Jack Berg** 24:20 Well, I don't know off the top of my head. Maybe not easy, but definitely possible.
**Trask Stalnaker** 24:24 I mean, I only know because in the Java agent, the implementation I added in the Java agent in order to implement these GET, simplified GET, oh no, actually, it was… in order to resolve it to a system property, I had to pass the breadcrumb down.
Because I have to resolve the system property at the leaf node, I can't resolve it as it goes.
**Jack Berg** 24:50 Yeah, so that, like, maybe we're not passing that parent down yet, but we totally could, right? And then…
**Trask Stalnaker** 24:57 For the message, like, it wouldn't have to be exposed publicly.
**Jack Berg** 25:01 Right, exactly.
**Trask Stalnaker** 25:04 And so the earlier… oh yeah, is the signal strong enough?
I mean…
I'm okay with the signal in terms of users are like, oh, it's not doing what I want, so, like, what's the first thing we'd do is say, check the logs?
**Jack Berg** 25:26 check these logs, we need to tell them, you know, what the…
You know, the name of the logger is, and what the pattern looks like, so… That's probably doable.
**Trask Stalnaker** 25:37 Yeah, I mean, I guess I hope that the logs surface in their normal log, like, I was thinking from without it having to come to us.
Like, if they have to come to us and ask us, then we've… then that is… problematic.
**Jack Berg** 25:56 Oh, the 9…
**Trask Stalnaker** 25:56 of it.
**Jack Berg** 25:57 Now we're dependent on the application logger, where the Java agent's logs get looped back into the application's logs.
**Trask Stalnaker** 26:07 Well, we have Java agent logs.
So, basically, I mean, from the Java agent side, if anything isn't working, like… Check the Java agent logs.
**Jack Berg** 26:22 Yeah. And it would be a warning.
**Trask Stalnaker** 26:25 And we don't log many warnings, I don't think.
So I would hope that that would stand out.
**Jack Berg** 26:34 Right, so, you know…
We have documentation that says this is where to look, and, you know, we make sure that we're logging at a sufficient severity threshold level to, you know, make it important to users, so that they're probably not filtering these out.
Because it really is a… it's a… it is a warning,
a warning is warranted. Like, this should be rare, and it's something that you should act on, if there's a tight mismatch.
And then the other thing that, and I talk about this in the comment here that you have on screen, is like, hey, so if the default is to fail gracefully, to, like, not throw an exception, then I think we should still provide the capability to, like, for the callers of declarative config properties to understand this.
Right, so if you want to fail fast, you, like, the API shouldn't preclude you. So we need to find, like, another mechanism where you can, like.
you know, ask the API, like, hey, what is the type of this thing? Is it the type that I expect?
But that's, like, secondary, because, you know, the… you know, the agent would… would not be using these APIs.
**Trask Stalnaker** 27:59 Yeah, do you… would you want to add these… Before stability…
I mean, because I'm kind of curious the use case… Still, like, if… Other people would use these.
**Jack Berg** 28:16 Yeah, I don't… I can wait for feedback, and honestly, I don't think… like… Maybe I'm just…
too in the thick of things right now, but stability, there's, like, a lot of things that need to happen. For not declarative config, the data model and the spec, but for the Java implementation of this to stabilize, like, a lot of things need to be shifted around.
And there's going to be a lot more questions about this. I kind of let… I have an issue somewhere where I'm tracking, like, hey, what is the final home for declarative config, the implementation? And, let's just say there's, like, there's some reshuffling that needs to happen, and yeah, so it's going to be tricky to get to stable.
**Trask Stalnaker** 29:02 Okay.
**Jack Berg** 29:05 So it sounds like you're leaning towards fail gracefully by default, like, don't throw exceptions, and like, you know, like I said, I'm fine with that. I just, you know, I like that we're having the conversation.
**Trask Stalnaker** 29:17 I'll open an issue. I didn't want to derail this PR, I did approve it.
Because it's independent conversation from this. But yeah, I'll open an issue to track and discuss further.
Well, if people aren't tired of declarative config.
Like, I have another declarative config.
topic… Yes.
Sort of, do… and,
This is… because right now, so this is sort of what it looks like for getting a declarative config.
property.
And there's…
you know, still a bit of boilerplate, like git config provider, get instrumentation config, get Java, that's gonna be on most of them. There's also get general,
Which is the other node that we would look at.
So kind of the question is, Should shortcuts exist for that?
**Jack Berg** 30:42 The get general is what I was forgetting about, because, you know, in this conversation here.
I'm suggesting that we add a shortcut for, like, getJava Instrumentation config. And, you know, this says, hey, I have the name of an instrumentation library, I want to, you know, get the config for it, or empty, if it doesn't exist.
And, you know, I was thinking that that…
allowed us to scrap your PR7920 trask?
Which stops returning, null from, you know, get instrumentation.
Confusion?
**Trask Stalnaker** 31:21 I'll have get general instrumentation config.
**Jack Berg** 31:25 Yeah, that's true, right? Okay. So, you know, basically we have shortcuts for the two common,
access paths that we expect in the Java ecosystem. Getting a specific instrumentation libraries config, getting, you know, general config.
I like that.
But, you know, like, my point was, if we can get rid of your 7920, and we have convenience methods for the common things.
Then, like, we can kind of have our cake and eat it too, because callers still have the ability to determine if it was, like, if instrumentation was not set.
**Trask Stalnaker** 32:06 Why do we care if instrumentation… if that top-level instrumentation node is there or not? What does that signify?
**Jack Berg** 32:16 This was going back to our conversation about, like, what is your signal to determine if, like, declarative config was used?
And I don't think it's that important, like, but, like, I also don't know if it will be important. And so retaining the ability to at least, like, determine if it was set seems, like.
Seems good, at least while we're still learning, as long as there are convenience methods to not have to deal with that null ability for the common cases.
**Trask Stalnaker** 32:54 Cool, yeah, I mean, we would never call… yeah, we would always use one of these two, so I'm…
Don't… I'm neutral on what happens to the… other one.
**Jack Berg** 33:08 Sounds good.
Next topic… Alright, so…
I opened up this PR back in October. It's a draft PR, and it sketches out what we would need to do to promote our senders to our public API.
So we can, you know.
Make guarantees about them from a stability standpoint.
And I think it's, we got good feedback from Bruno. Bruno, like, went and worked off of,
This branch, and, you know, updated the…
the Quarkus implementation to be off of this and set it like, hey, this works, our tests pass, and, you know, like, the concepts make sense.
So that's good. And, so the next steps for us, and I think I mentioned this at a JavaSig a while back, is to determine, like, you know, just what… what we want to do to actually get this from, like, a draft to merged.
And, you know, the two key things we can do is, like, we can do it in one big PR, or we can do it in chunks.
And if we do it in chunks, though, we need to figure out a way to have all of those chunks merged in one release cycle to reduce the churn.
So, yeah, that's kind of the trade-off. One big PR is harder to review, chunks, like, are sort of going to mean that we have to do, like, commit to getting all the chunks done in one month.
Or use something kind of unique and one-off, like a working branch, a feature branch that we're merging the chunks to.
**Trask Stalnaker** 35:06 Let's see, is this too big? It's probably too big for, Github to split out
I don't know if you've seen on smaller PR, on normal size, but normal-sized PRs, GitHub, at least in this new PR experience, it'll break them out automatically into pieces to review separately.
**Jack Berg** 35:30 Really?
**Trask Stalnaker** 35:32 Yeah, yeah, let's find one that's… Not massive.
But also not tiny.
**Jack Berg** 35:39 It's right in the sweet spot.
**Trask Stalnaker** 35:43 Probably too small.
Yeah… Oh well. Look, yeah, keep your eye out.
I haven't found it super useful yet, but I'm hoping it will be.
become more useful.
What would… how would… do you have a thought how you would split it out, if you did?
**Jack Berg** 36:12 Yeah, it's things like, you know, like, if you scroll through these files on the left side, it's like, okay, promote the compressor.
to the stable API. And, then, you know, rework the gRPC side of things, rework the HTTP side of things, and, like, rework the martialer side of things.
And kind of do these things successively.
But,
I guess I don't have the complete path in my head, like, laid out. I know there is a path to break it into smaller chunks, I just don't know the most natural path off the top of my head.
**Trask Stalnaker** 36:57 I think it's hard for us to…
commit to getting things all in a, like, multiple PRs all in a release.
So… I feel like I would…
suggest… I mean, even with the best of intentions, you know, things happen.
**Jack Berg** 37:18 Right.
**Trask Stalnaker** 37:18 so, I'm… I'm not opposed to the feature branch.
**Jack Berg** 37:30 I can do that. Not, you know, it…
I guess it can be a branch on OpenTelemetry Java, or on, like, you know, my personal fork.
**Trask Stalnaker** 37:42 Oh, that's true, because we have branch protection rules that are going to be annoying.
**Jack Berg** 37:53 But these are all just tools for us, right? Like, so, like, even if we have to have a feature branch on my fork.
you know, like, we can kind of just trust that I'm not gonna touch that feature branch, except through PR mechanisms.
And, you know, then when, like, when it comes time to merge the whole feature branch into main.
You know, you know, we trust that each step was done right, so we trust that the whole thing is… is good.
**Trask Stalnaker** 38:24 I like that. I… I really,
struggle to review these massive PRs and, would be… Much more, yeah, so, that's my two cents.
**Jack Berg** 38:44 Okay, I'll plan on doing that then, and then we kind of don't have to rush and try to get it done in a month.
And I don't know, maybe, like, we haven't done this pattern much before, like, you know, using feature branches, so maybe we'll like it, or maybe we'll hate it, and we'll learn something.
**Trask Stalnaker** 39:04 Yeah, I mean, normally, in most cases, we can find ways to break it, break things up.
And… Still, for them to be, not block a release.
Right? Sort of things that are, like, more iterative.
But for public API, I feel like public API is where that whole thing, and avoiding churn is where that
Hmm, falls down.
**Jack Berg** 39:36 Yeah, it's kind of a unique set of circumstances.
**Trask Stalnaker** 39:43 Like, I don't know, like, could you hide, could you do things, but… Yeah.
Hide them under different… package names, I don't know. No, not really, like…
Yeah, it just doesn't work well.
with public API.
**Jack Berg** 40:02 Yeah, like, of the 1500 lines, almost all the lines are, you know, just restructuring, reshuffling around of things. There's not, like, functional changes in here, so,
It's, it's pretty close to the… Like, the minimum.
That you can get in, like, in one big PR.
Even if… even if there's, you know, subsequent internal refactorings later.
**Trask Stalnaker** 40:39 That's a good point.
That definitely makes it easier.
To review, trying to think if this is something that…
Is it ready? Like, this is your…
This is in final form here.
**Jack Berg** 40:58 There's, there's, like…
there's an hour's worth of work I want to do on it once, like, before I open it up from a draft. There's, you know, one little change that Bruno and I talked about.
In the feedback, but it's pretty close to being ready.
And it's just about, like, hey, it's actually this specific thing. So, OTLP responses.
Like.
We don't do anything with them today, but they do have content in them, and so the question is, should our abstractions that we're introducing, like, be future-looking, and force you to have… force the sender implementations to have to return the response body so we can do something with it in the future?
And, that's the only change, is like, you know, questions about that.
**Trask Stalnaker** 41:52 Will that, impact many files?
**Jack Berg** 41:55 No, no.
**Trask Stalnaker** 41:56 started… okay.
I will let… before you do anything, break anything out, I'll take a…
Half hour today, and start, kind of, like, cause…
Now that I'm looking, like, now that you mentioned, like, it's just so much of this is structural, I'll go through and, like, you know, do the whole viewed thing, and see what I end up with, like, in terms of what's remaining of things that actually I need to look at more carefully.
**Jack Berg** 42:28 Yeah, maybe it's not scary after you, like, filter out all the structural… Yeah.
**Trask Stalnaker** 42:33 Yeah, yeah.
Yeah.
Cool.
We'll chat.
**Jack Berg** 42:40 stress.
**Trask Stalnaker** 42:46 Alright… Emmy… Last topics for the year?
**John Watson** 42:53 I have a… I have just a quick question. I gotta ask internally.
about setting up the Prometheus?
exporter to support HTTPS.
Rather than just HTTP, and was looking through the spec, doesn't seem like there's any support for it in the spec, and it doesn't look like there's any way to do it.
With our… like, using the agent, using,
any of the existing facilities to make that possible. I was wondering if anybody had looked into that at all, or run into that.
**Jack Berg** 43:27 I bet you could do it if you were okay with having a customizer.
**John Watson** 43:31 Yeah, yeah, no, I… exactly. It was more… I'm sure it could be done programmatically. Anyway, out of the box with our existing configuration options?
If anybody had run into that request.
If not, it's fine. Just, I was a little bit surprised that we didn't have any way to do it, and there wasn't anything in the spec about it either.
Especially as we're getting lots of requests, like, you have to use HTTPS everywhere internally, and… Even on the… even local to local host to local host, yeah. Yeah, yeah.
**Jack Berg** 44:06 That's… that's, that's interesting, because, like, the environment variable spec for Prometheus is just… it's really narrow. There's just two, like the port and the host.
And declarative config, there's, like, I think 4 additional options or something like that, and none of them… I haven't heard any conversation about HTTPS, so…
Yeah, it hasn't even entered the picture.
**John Watson** 44:29 Yeah, I was a little bit surprised that that was the case, but I guess it's rare that people are asking for it, but… I was also, like, they're like, well, yeah, we haven't turned OTLP on in our collector. I'm like, why not? Like…
Your collector's there, just flip the switch, and away you go, it's easy.
Anyway, that was, just thought I'd ask the question if anybody run into it.
**Trask Stalnaker** 44:55 We don't have, Gregor. Might be worth asking Gregor.
I've heard of the request. Oh, you are Gregor? Oh, you are Gregor!
**GZ Gregor Zeitlinger** 45:06 Yeah, but I'm on my phone, that's why I did not participate much.
**Trask Stalnaker** 45:11 You were hiding behind those clouds.
**GZ Gregor Zeitlinger** 45:14 Exactly.
**Trask Stalnaker** 45:17 Do you know… have you heard of,
people wanting to do Prometheus scraping of the Java agent over HTTPS.
**GZ Gregor Zeitlinger** 45:29 Never, I also have not heard it in the context of Prometheus,
Java SDK either, even though it's possible, but never heard the question.
**Jack Berg** 45:45 That's an interesting signal.
**Trask Stalnaker** 45:47 Do you have a sense of how many people are scraping, the Java agent scraping the Prometheus versus sending it to the collector?
**GZ Gregor Zeitlinger** 46:01 No, I don't.
I don't have stats on that.
**Trask Stalnaker** 46:09 Yeah, I don't have any sense for it. I'm just trying to think of reasons why
That wouldn't have come up.
But you said it is, in the Prometheus SDK itself.
Is it supported?
easily, or do you have to, like, set up a SSL context, or do something more…
**GZ Gregor Zeitlinger** 46:31 It's easy.
**Trask Stalnaker** 46:33 Okay.
**John Watson** 46:34 I mean, if you want to have…
In your own certs, you'll probably have to do things a little bit more… Clever, but, yeah.
**Trask Stalnaker** 46:44 Okay.
**John Watson** 46:46 Anyway, just thought I'd ask. Not urgent, but yeah, just thought I'd ask.
**Trask Stalnaker** 46:54 Alright then.
Enjoy the, the… OpenTelemetry holiday.
**Jack Berg** 47:04 See you all in a couple weeks.
Yeah.
**Jay DeLuca** 47:06 20 years.
**GZ Gregor Zeitlinger** 47:07 Have a great time!
**John Watson** 47:11 Bye, everybody.
