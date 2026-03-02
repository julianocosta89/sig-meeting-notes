SIG: Semantic Convention Tooling
Date: 2025-07-23
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/ONasIMNrXnuvOGulU5-quFR8Lnv_1yDgrwr-6OIUDzapLanzMgSV60tqoSCF07Uy.wxItpNXTxszJLD80
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 00:19 Hey! One hello!
**Josh Suereth** 00:28 Okay.
**Laurent Quérel** 00:57 So what are the news?
**Josh Suereth** 00:59 What's the news? While you're out.
**Laurent Quérel** 01:04 Yeah.
**Josh Suereth** 01:07 What did we talk? Oh, I'm not presenting it. Man.
I'm not sure. I'm not sure what to what? What
how to answer that there's so much craziness going on in the world in general.
**Laurent Quérel** 01:24 Yeah, I can imagine I follow the news in the world.
I didn't follow so much the news, for we were during the last 2 weeks.
**Josh Suereth** 01:35 The thing. The thing that makes me saddest in in the recent news is, I love watching Stephen Colbert, and so they
canceling that show. So I'm hoping that maybe he joins Conan O'brien on a podcast or something for
because because that's also something. I enjoy listening to.
**Laurent Quérel** 01:55 Yeah, I agree.
**Josh Suereth** 01:56 Anyway. Yeah, the big thing. Schema, v, 2, planning. And then
this was how to we have. We have a couple proposals around defining like,
we'll we'll go through triage quick. Actually, let's do that. And then I can. I can show you what we talked about, because I think it's still there.
**Laurent Quérel** 02:19 Okay.
**Josh Suereth** 02:21 In semantic convention tooling.
Just to look back at this of what we're doing with decisions and things.
introduce span identity can be used by consumers is still a big to do.
As far as I know. I think Ludmilla had a proposal for this, but we we haven't actually made
progress on making that happen in like Oteps and things. But that's something that still needs to get done.
I don't think anything necessarily happened on here outside of. We're trying to clean up the Yaml schema
with with various things, and there were some proposals around attributes that we could have on the Yaml.
I'm gonna I think none of this is really worth talking about right now. So I'm gonna skip to our other triage weaver board, because that one
to consider for next release. And no status does this have all the new stuff in it? I didn't import recently
attributes. User attributes. Scope should require attributes. Yeah.
there's there were a bunch of proposals around like weaver schema the about.
And this was also in semcomf
around the idea of namespace and namespace documentation.
So there'd be a group called namespace that would have like a header and a footer and a body.
And there was a bunch of discussion around that. There's a proposal in semcal around what that looks like. We're basically
we want to understand what the goal is and what the end result is, and I think that I recommended in the Prs. To make a proposal like your application
telemetry, schema proposal, and multi
resolution proposal like, I think a lot of those Prs need a design, Doc. So that was
I think that was the big, the big discussion there outside of like next step. Things
template extension, weirdness for weaver registry diff. I don't think anything happened there. Generate Json Schema from rust models. I haven't had a chance to dive into that. But I have a topic today to talk through. That
weaver should resolve the full URL to do.
I'm not sure what this one means.
Oh, this is when we get a link path.
We probably Ludmilla wants us to resolve it to the URL of the thing we pulled in when we're pulling in a remote repo.
I believe, like we might need to expand links in some fashion. I'm not sure how we do that.
**Alexandra Konrad @Elastic Security** 05:23 I think we need to provide the full URL like resolve the full URL. Otherwise it breaks.
**Laurent Quérel** 05:29 The or something like that, or the
some kind of control into semantic convention that look at the do you own?
So maybe what we can. So I guess it's related to Code or Doc. Generation.
**Josh Suereth** 05:50 Yep, I think if we look at this here.
**Laurent Quérel** 05:53 So we could imagine that it's basically a parameter into the wearytml that can be used.
So we we just put the the base URL
into the the we very Ml. As a parameter, and we
each time we introduce a link we
we can cut that with the base. URL. Will that be enough?
**Josh Suereth** 06:16 I think that's what they're suggesting here. The other possibility is, maybe
the other possibility is, we have some kind of a when we specify the repository and the repository information
for for Simcov. We would have a Doc Baseline URL for links.
So anytime you get a link in a brief or a note. It assumes that that
is relative to some baseline URL that we give you.
So for for example, let me
alright. Well, maybe we could type it here.
spending relatively close to weeks
this, let me make this a little bigger.
So if I recall correctly when when we define a registry, do? I can't remember the syntax off the top of my head. I'm sorry.
**Laurent Quérel** 07:25 We do a generate something.
**Josh Suereth** 07:29 Yeah, when we read regenerate, it's like registry or something, right?
**Laurent Quérel** 07:32 Yeah, registry generate.
**Josh Suereth** 07:36 We have registry generate right? But we it'd be something like you would run weaver registry, generate, you know, docs
base URL equals dot Dot. But then, what I'm suggesting is then the resulting resolved Schema
would have
That's what I'm trying to remember.
**Laurent Quérel** 08:02 Dash, dash param equal
**Josh Suereth** 08:09 Right. I'm actually, I want to be a little bit more aggressive. Here, Lawrence, let me let me give me one second, because I need to remember the syntax. I was just looking at this, so I should remember. The registry that we define has a URL group count group that stats. Registry is a registry, URL, and groups right? So when the resulting schema is registry, which is registry.
URL and groups right where we have dot dot. That's what we have today.
**Laurent Quérel** 08:41 Yeah.
**Josh Suereth** 08:42 So instead of just so, basically, what we would have registered URL, is where you get access to this document. Right?
So registry Doc base URL would be something, and when you resolve a link in brief, or notes, or whatever
we would know, to replace the baseline URL of that link with the registry that it came from. So like when I advertise. Here is an open. Here is a registry right?
And that registry has information about contents and things. I'm giving you a URL where I am hosting
either the Markdown files or the HTML, or whatever
for, where, where, where to link things to I like. I'm still.
**Alexandra Konrad @Elastic Security** 09:31 I think sorry. I think the problem is that we need it when we release it. So it means that it's it should be provided for released. Yeah, data.
**Josh Suereth** 09:47 Well, that's that's why it's here.
**Alexandra Konrad @Elastic Security** 09:49 Hello.
yeah. But this this URL is not the release. URL. This URL is just whatever. So without release note, you know, I just.
**Josh Suereth** 10:01 Would be the release hero. So when we generate a release.
**Alexandra Konrad @Elastic Security** 10:04 Tomorrow.
**Josh Suereth** 10:04 So let's talk about going forward right when we generate a lease for semantic conventions.
we're going to be generating, resolve, schema.
going forward like in the long term.
So the idea would be when you generate your resolve, Schema, you would pass the location where you're going to host the Markdown files for that resolve, schema, and point people at the resolve. Schema.
I still, I still don't think we have a good solution to this at all like I, even with what they're suggesting, even with like putting it at like a github. Uri, I'm not
very happy with what I think. This will be still broken in various ways.
And this proposal I'm giving, the more I think through it, the more it's still awkward as heck. I mean, it could work. It's just
what if you're not exposing Markdown? What if you're exposing? HTML, right. All of the links that you have locally are marked down?
It's kind of a.
**Laurent Quérel** 11:00 But yeah, to to be honest, the the thing I'm not following is why the
what could already work today is not good enough.
Why, having a parameter and asking templates
to just use this parameter to define the base URL for each of their link, independently of the type of the artifact that is generated. It could be a markdown. There is a specific syntax for Link.
It could be an HTML. There is another syntax could be something next.
I mean, it's up to the Complete Hotel to define how to to make those links
related to to the not related to make them absolute
by using the the base ui, provided as a parameter.
**Josh Suereth** 11:54 It. How does that work, Laurent, when you have multiple repositories.
have to have them pick the right like.
**Laurent Quérel** 12:06 So. So if you, I'm not sure to understand. But if I understand where you want to generate the same, let's say the same documentation in different repositories.
**Josh Suereth** 12:16 Yeah, like, let's say, let's say I'm making a repository that uses Simcov.
**Laurent Quérel** 12:23 Yeah.
**Josh Suereth** 12:24 And defines new telemetry, and the docs that I get from Semcov.
The links I get are relative from from because I'm inheriting those attributes. I haven't changed them, and then I publish my schema, and it publishes with all these relative links. But it looks like those are relative links to my local repository. But they are not because I'm
depending on some right. So it doesn't transitively work.
**Laurent Quérel** 12:49 So it's in the context of meteoragistry
that you. You have this issue.
**Josh Suereth** 12:56 Well, I that's the reason I don't think what like a simple issue works here is because of transitive repositories
like, that's why my thinking is, we should probably think about a way to either make sure that weaver registry generate cleanses, relative links so they can be used in transitive dependencies.
or we need a way to basically update all relative links it when we resolve to make them absolute.
Because I like, I I think, relying on relative links
would. If if the resolve Schema tells you where relative lengths are relative to, and we keep track of like the origin of where things are and like can link up that way. Cool, we have a solution. But but if we start having like attribute gets inherited here, and I want to link back to that thing. There things start to fall apart. So
I don't want to make this complicated.
I want to have a trivial solution if possible.
But I also want to make sure that solution works with multi registry.
**Laurent Quérel** 14:08 No, okay. Okay.
Understand?
Because the the initial what? What you showed us before. I guess it does not care about meteoristry. But I understand that you want a solution that will be that will resist the the future.
And the future is soon because we want to be in the yeah.
**Josh Suereth** 14:30 Yeah, it's basically, if if there's no way to take the proposal and make it work with multi registry, do we want to take the time to implement it. Now.
**Laurent Quérel** 14:38 Yeah, yeah, I think the so in that case, it makes sense to to have a way during the the resolution process. So in instead of using. So the in that case it will be more. We have a registry resolve.
dash, dash, dash, dash, Doc base! URL equals something, and then we inject
these days we are into the the fully resolved schema. And when we import
so we need to to also to to change the way that media registry is currently addressed.
Because right now we we plan to. When we do an import, we import a registry as.
**Josh Suereth** 15:26 But I don't.
**Laurent Quérel** 15:26 Non-reserved registry.
We know that we want to import the reserve, because that's basically what we we are trying to achieve. So what? So what you want to achieve. We require to support
import in mutual registry context, that import visual registry. Then we will get this
a base URL per registry that we just discuss that we could introduce, and then code, generation or document generation could leverage this information
because that will be be visible by Weaver for every transitive dependencies. Like you said, Yeah, personally, I like the the
I like the the approach.
I think we need just to to see how to maybe unserve that in a so we have a
a long term vision. When I say long term, it's not necessarily super long. But let's say we have a a vision to where we want to go. And in between, do we want to know that now that we we have a good solution, are we able to do it
temporarily in the current situation where we don't import result registry, I guess.
**Josh Suereth** 16:45 We we could. I I'm
I want to talk through this, but I want to defer some of this stuff. The
version, 2 of the schema is going to be rather aggressive, and I want to talk through some of the architectural changes I want to make. But I really really don't want us to be mucking around in there with more than one project at the same time.
**Laurent Quérel** 17:08 Yeah.
**Josh Suereth** 17:08 So like when we look through this one of the things that I I want us to consider like these to be considers for next release. We might want to put some things onto the backlogs, because I want us to get out. Resolve schema and telemetry schema 2 point O. As quickly as possible. I think we need to be laser focused on getting that out. The door.
**Laurent Quérel** 17:26 Thank you. David.
**Josh Suereth** 17:26 It's up to date. And so like.
this is a friction reduction thing that yes, we we should be able to do. I think you can solve it today with just parameters and Cogen.
**Laurent Quérel** 17:38 Yeah.
**Josh Suereth** 17:38 Java like they can do that right. That's that's something they can do. So we have an idea of what we want to do in the long run, I think we should not have it to consider for next release.
**Laurent Quérel** 17:49 No, I think what we should do is maybe a Github issue describing the solution
that we attach to the the Schema. V. 2. Initiative.
And so we keep track on that. And and we focus. Only I fully agree with you that the scheme may be too.
And but yes, we have a we. We track the
that we describe the the future evolution, and we and we track that in this initiative. So at the end of the.
At some point we will say, Okay, now we know that we have the schema. V. 2, how to integrate that into media registry. And then that's where we will start to import scheme, resolve schema
instead of standard or basic auto-oriented registry.
Yeah.
yeah, I I like the personally, I like the approach, and I also like the idea that you you just mentioned regarding.
**Josh Suereth** 18:50 Yeah, okay, I'll add that documentation. Then. Sometime after this meeting, I want to get to a few other things. So one thing related to what we're just talking about this this thing here. This was the namespace thing that we deferred. I basically said, I asked for. Let's get a design phase. I pointed out your design for multi registry support as an example for this thing, because I want to defer it. There was also scope.
And I want to want you to see this comment here. So basically.
this is about instrumentation scope, which I think is mostly unused in Weaver and Semcov. I prefer, if we don't add any scope dependencies.
or or change how scope works. I'm actually planning to ignore it relatively for V 2 initially to get V 2 out the door, and we would define it later, because we actually haven't really thought through it.
So I I would like to basically say that we are not entertaining changes to how scope works in resolution today. Just so the refactoring work doesn't take longer
right because we're no one's really using scope today
that I know of. Yes, it exists in Weaver. But we we aren't using it in semcom. We kind of don't really have well defined rules and things around it. And I think it needs a lot of thought. And so I just kind of want to say we're not accepting scope, related, things right, now.
**Laurent Quérel** 20:19 Yeah, okay.
**Josh Suereth** 20:22 Cool. I'll continue to push on that. There was a there was a really good Pr. I want to call out here on a usage section. Please take a look at this. I approve this.
it's it's yet again more interesting fixes to the readme.
So this one
The only complaint I have is some of the links that we had before are just gone.
and I I couldn't tell where they wound up overall. But basically, this, this focuses, it takes what Jeremy had done and focuses on
making things a little bit cleaner. This is someone who used weaver. And they said they wrote this based on what they wanted in docs when they onboarded so but I think there's some good stuff here like working with real telemetry, live, check, and admit.
**Laurent Quérel** 21:14 I wouldn't know.
**Josh Suereth** 21:15 Generation validation and comparing. It's it's pretty cool. And then they also added.
and I like this, a whole code generation section that talks about high level overview. It links into forge, and it has a very nice diagram of like what is happening
in weaver generate that really describes things. So so I do really like this, Doc. I think there's some cleanup to do. But given, this is a 1st time contribution.
I would be happy if we just merge this as is, and clean up ourselves some of the things we'd like to clean up if folks are amenable. But I wanted to run that by Laurent and Jeremy.
**Laurent Quérel** 21:53 Okay, I just open the tab on this and I will look at it later.
**Josh Suereth** 21:58 Okay?
Yeah, I think validate also had. Yeah, this one, this one, we can start flushing out more. But Jeremy does this is this in line with what you wanted to get out of the readme going forward like, do you think this is a general moving forward, or is this moving backwards.
**Jeremy Blythe** 22:15 Think it's moving forwards.
Yeah, I did. I did go through. And I I nearly did approve.
Nearly
**Josh Suereth** 22:25 It.
**Jeremy Blythe** 22:32 Some things are missing. I guess it's good as an iteration. Let's let's put it that way.
**Josh Suereth** 22:37 Yeah, what I'm proposing here, because I agree with you. Some things are missing, and they explicitly call that out. Given. This is a 1st time contributor. If if you, if we're all are willing, if someone can shepherd this Pr, I would prefer to merge this.
Have us make the changes that we need, that we that we decide like the missing pieces quickly and like CC, them on the changes. So they're aware of, like what we wanted to see going forward, but, like encourage them, continue to continue to provide documentation.
**Jeremy Blythe** 23:08 Yeah. The only thing is.
I was. I liked the thing, the thing that Laurent did like really recently, and I put that as a how to which was, I can't remember. You did a how to on
whatever it was. Can't remember now, anyway, did the how to and that was really nice.
There we are. Define your own telemetry schema. That one.
**Josh Suereth** 23:31 These are these are still there, I believe. Yeah.
**Jeremy Blythe** 23:33 I just wonder whether some of those things.
because this author has written their their take on
code generation like from their perspective. It's not like this is the
everything that code generation is about. It's like.
here's my take on it. So it feels like, maybe it should be more of a how to from their perspective.
**Josh Suereth** 23:55 I see. So you want this like a how to code generate.
**Jeremy Blythe** 23:58 Like it could be a how to like.
you know, cause it. That's exactly how they described it in the
in the pull request is I needed this because this is what I was doing.
not get documentation. That explains everything that you can do that makes sense.
**Josh Suereth** 24:15 I gotcha. Okay.
**Jeremy Blythe** 24:17 So how to can be more sort of narrowly focused on a specific thing.
whereas the the usage section really is like, here are all the things.
**Josh Suereth** 24:30 Okay, that's fair. That's fair. I mean, I I'm
when I reviewed this I see this as an improvement, because it gives people a way to get started that makes sense and kind of calls out how to think about it and what to do.
And then we would expand this over time to be complete.
**Jeremy Blythe** 24:55 Okay. But if you.
**Josh Suereth** 24:56 You're saying that this would only ever be a use case, then I'd agree it should be in a how to.
**Jeremy Blythe** 25:03 Yeah, I mean, you could go either way, I suppose? Right?
**Josh Suereth** 25:06 Okay, that's why I'm asking, like, I think one of us needs to take this and shepherd it. And
my proposal would be, we merge it
to, to encourage the developer, to continue to contribute. But one of us would take it then, and flush out the pieces that are missing
as like an immediate follow up
**Laurent Quérel** 25:26 You you mentioned? Links that have been removed?
so you you return some back about that or
**Josh Suereth** 25:36 I? I asked them to. I think this main commands thing should stay in the main Readme.
So I would prefer to have it there, because I think it's it's actually valuable. This documentation. Oh, the main command. Sorry did stay this documentation here. I want to make sure all of these links are still somewhere.
**Laurent Quérel** 25:55 Okay? So I will take attention to that during the the review.
Okay?
Cool.
**Josh Suereth** 26:03 I think that's all I wanted to talk about for that. And then oh, no one else has an agenda item I have. I have one that I want to talk about. This is going to get nitty gritty. If that's all right with everybody, I think we don't have anyone who isn't an active contributor. So that's
that's good. You ready for the nitty, gritty talk.
**Laurent Quérel** 26:22 Yes, just when I forget to add my own entry there. I just want to add it before we start. So you you have a
oh, no idea yet. Yeah, I want to talk about multi registry.
She bought on more than 2 levels
because we had this discussion a few days ago with Jeremiah, and I just want to make sure that what I have in mind.
We are all in agreement with it.
**Josh Suereth** 26:58 Yeah.
Okay. So, Lauren, you missed a few discussions here. But basically, we're planning to add a version column to semcom spec.
I have a prototype. Where I have 2 rust structs. One is a top level semcom spec
that has 2 untagged enums, one which would be this semcom spec and another, which is a version semcom spec. Then I have a second rust struct which is the version semcom spec, where each enum is tagged by the version number. So you would have version Colon 1.0 would resolve exactly as is resolved today, and version Colon 2.0 would use the attributes, metrics
scenario that that Ludmilla promoted.
**Laurent Quérel** 27:49 Okay.
**Josh Suereth** 27:50 That's the context. I can show you. Actually, I can't show you that code because it's on my other computer.
And I forgot to push it to Github before the meeting.
**Laurent Quérel** 27:59 Yeah.
**Josh Suereth** 28:00 So apologies. But the, the. So that's the context. Now, what I noticed in here, okay, is, we have a bit of a architectural confusion from file here for Samcom spec.
Does a few things. It will read some conf file, and it has the new Json schema validator that uses the Json schema
from Json schemers. Right?
This is the only place that works. It doesn't work on string from string, and it doesn't work on from
What's the other one from URL, right.
**Laurent Quérel** 28:47 But but
**Josh Suereth** 28:48 From URL does not have it.
**Laurent Quérel** 28:50 Okay.
**Josh Suereth** 28:52 It has validation, but it doesn't have from string. Then we also have semcom spec with provenance
where it tries to track the provenance of whether it came from a file or not? And does the validation.
Okay, and from string, and it does not have from URL.
**Laurent Quérel** 29:13 Yeah, you know what I think. It's
lack of cleaning in the code. But I will be interested by looking at if formula is used at all, because, in fact, the the way that we.
**Josh Suereth** 29:28 It's it's not I. I already looked it up.
**Laurent Quérel** 29:31 That's why. Probably I didn't report that on.
**Josh Suereth** 29:36 Well, it's it's this is used in tests, and this the from string in here is used in tests. A lot
from file is only used in from file here.
So what I want to do if it if everyone's amenable, I want to gut the crap out of this, and I want to have exactly one like resolution like, I don't.
I'm planning to. If it's okay with everybody, remove all of the helper methods on on semcom spec
outside of test only like configuration, things that might resolve from a yaml file.
Okay. But like the validation work, all that kind of stuff, I'm going to remove a dependency on these helper things I'm going to get. I want to gut all of them and have one path down through the hierarchy, because I'm going to start having that diverge. I'm going to have this new
top level semcom spec that will let you do the version matching.
And then, additionally, when I do that, my plan is to take this Json schema part here
update this to, instead of being a schema just for simcom spec being a schema for both versions.
**Laurent Quérel** 30:54 You know.
**Josh Suereth** 30:54 And find a way to make this work for things resolved from a string temporarily, because
I found that test error messages without this was awful. But when I included this for test error, messages, things were better.
But when I was going through and writing the code it became really really ugly. Spaghetti.
**Laurent Quérel** 31:16 Yeah.
**Josh Suereth** 31:17 So I might send a pr initially that that guts this and cleans this out as a separate task first, st and then I'll start continuing the the V 2 schema work.
**Laurent Quérel** 31:29 So I have 2 feedback in that. So
I think in general, I understand where you want to go and agree with the
I'm not sure I agree with you but that the the approach
let me detail. So the 2 things you remember at some point when I was working on what it was.
Oh, well, on the import, the regarding the
when we were able, in a meeting registry context, to import matrix signal from the imported registry, so that the work I did before my my videos.
**Josh Suereth** 32:14 We.
**Laurent Quérel** 32:17 Let me see how to present that.
Yeah. In this context, what I did I started to explore, but I didn't include that in the in the Pr. Because it was
too big, and I didn't want to spend too much time during the review. So I put aside the beginning of a work I did which consists to
us apply a more structural approach
for ultimately convention spec and the corresponding groups.
so representing groups as with volume that are specific to each signal in order to avoid the the
the fact that we merge all fields in one script. So I did this effort. It's it's some.
**Josh Suereth** 33:07 Mode.
**Laurent Quérel** 33:08 On my computer or in a branch.
So the question is, should we 1st do that? And then you do your stuff.
**Josh Suereth** 33:18 No, because that's what v 2 of the spec is like. Like. Again, I I think we want to get to v. 2 as quickly as we can.
**Laurent Quérel** 33:24 Oh, okay. Okay.
**Josh Suereth** 33:26 If you remember this, this is another thing, we should probably talk through your comment. V. 2 of the spec is, I have an entity group.
I have a metric group.
**Laurent Quérel** 33:37 Item.
**Josh Suereth** 33:37 I have an attribute.
**Laurent Quérel** 33:39 Okay.
**Josh Suereth** 33:39 I have an attribute death, and they're they're all explicit. Yeah.
**Laurent Quérel** 33:44 So second comment is so. In that case, second comment is, I think.
to achieve the goal of adding schema. Version 2,
we, my initial understanding was, we want schema version 2 for the resolve schema version of it.
It's not what you are doing right now. What you are doing is for
the auto version of the the schema registry right.
**Josh Suereth** 34:17 Yes, so so what? It so, Lauren? I.
**Laurent Quérel** 34:19 For me the the most direct path to achieve what we want.
**Josh Suereth** 34:23 No, I am starting with this because I
this is the thing everybody's writing today. This is the danger. If everybody's writing on Schema. v. 1. It takes us a longer time to get rid of schema. v. 1. And so I want to resolve that first, st because I think it's both ease of use, and in doing so
we will get practice with whether or not these structures and shapes matter for the resolve. Schema, if resolve schema has no users, but the other side has tons of users. Right? I'm going to focus on getting the model right on the left hand side first, st and then do resolve schema. So the path I'm taking is this, first, st then, resolve, schema
and formalizing resolve schema. But I want to be able to confidently go when we say resolve, Schema looks this way and say, Look, we have proven out that this shape works.
and that this is how we should do it in the hotel spec. And here's all the people using it. Right? Here's what it looks like in Sem conv. And we have people who are like, Yeah, I understand that shape. I understand why it works that sort of thing. So I get what you're saying, and I know we want to get to resolve Schema quickly. I see this as a kind of needed dependency to shift how people think about
writing the semcom to begin with, to match what we want, resolve schema to be. I actually think this will simplify in the long run everything. And I want to make sure that I can go from the V 2 input to the V 2 output.
So I'm with the V 2, input, I'm going to do the V 2 output next. But 1st is, I want to get a Pr that shows this, that has the 2 versions that can resolve everything and can generate this
so that semcomf can start actually adopting the model immediately.
**Laurent Quérel** 36:13 Okay.
**Josh Suereth** 36:14 Then and and think about that. So then, Semcom is adopting that model. They're fleshing out. We have. We can even make a policy that requires version 2, right in semantic conventions at some point.
so that things like attribute group and extends are things I can completely ignore in resolve schema.
If I need to, to make things work. So that means that like there might. There's a chance that I ran into when I was trying to design the resolve, schema, that there are things you can express in v. 1 that are unexpressible in v. 2.
And I don't want to keep any of those things, because I don't think there was value in that expression.
I think it just made life complicated for us as implementers and for users. So I just want to get rid of that completely.
So if we can actually make it so, you can't express it anymore in v, 2, and we move suncom to v. 2.
I can now implement this resolve scheme, and everything's good. That's my! That's my rationale. There, now that you're back, I want to make sure we talk about it, though.
**Laurent Quérel** 37:17 Yeah, okay, I understand. So in theory, it's not the fastest path, but it's the the path that will give us more insurance on adoption and validation of this totally understand, I understand, that
makes sense.
But so the so the
when you were explaining that I was thinking, oh, now we need to generate 2 Json schema, one for the version, 1, 1 for the version 2. And when the the validation process that you you mentioned that was super useful.
based on the Json schema. Validation we recently introduced now needs to be.
**Josh Suereth** 38:04 Yeah, so.
**Laurent Quérel** 38:05 With 2 different schema.
**Josh Suereth** 38:07 No, no, what what we have, what we have, Lauren is we have this we have.
I'll just show you, because it's on my other computer
untagged. I think. So. There's an Inu top level Semcov spec
that has a v 1 schema.
Or sorry, it has untagged or unversioned with v. 1 schema.
And it has versioned with v 1 or version schema.
Okay, then we have a enum for versioned schema.
and we have, I think it's like 3, rd you know, tagged equals version something like this.
I don't remember the specifics, but I have. This one has v. 1 sorry
3rd tag equals one dot, OV. 1 is semcom spec, and v. 2 simcom spec.
D. 2. Let me make sure that I update this to be correct. This is what I implemented and made some Gson.
I generated this. I generated the Json schema off of this right?
And so that gave me actually pretty good error messages with what you had done. I just changed the Json schemars to be on this thing instead of on semcom spec.
And I'm doing this untagged enum where it picks on version versus versions.
And then inside of version, I make sure there's a tag, that is, one dot o and 2 dot o.
and we can. We can add new versions if we want going forward. I could also do version one and 2. This doesn't like I don't care if it's 1 and 2 or 1.0 2.0 don't care. It doesn't matter. The point being. That's that's what I did in the prototype, and I was able to get pretty decent error messages as soon as you put version 2. The error messages you get are way better because of the.
**Laurent Quérel** 40:25 Is well defined. Yes.
**Josh Suereth** 40:26 Yep.
**Laurent Quérel** 40:27 Yeah, and a lot of validation that we did for version, one will just be removed, because the
because, in fact, it's validated by the reason, schema. The fact that we can't use, for example, metric 10 for span, was part of the group validation. We no longer need that.
**Josh Suereth** 40:43 Yep, yep. I mean, what I'm doing in the prototype is I'm actually converting version 2 back to version, one groups running through the validation.
**Laurent Quérel** 40:51 Validation, but in fact, they will never be triggered. Yeah.
**Josh Suereth** 40:54 Exactly exactly, and that. And then once we get the right hand side onto Version 2, we have to keep things in their current state for some time until we get everybody onto Version 2 for their definitions. But as soon as we can get rid of some of that code in the middle. I really want to do that.
**Laurent Quérel** 41:11 Yeah, we now we need to think about how to support previous existing semantic convention registry
that are obviously still in the previous model or schema
so if we want, we were to still support the one dot 31 dot, 31, and so on. Maybe we have to keep that. Fortunately for.
**Josh Suereth** 41:37 I think we keep this for quite some time. Yeah, I mean, it's that's why I want to get this out quickly is so we can stop supporting those longer term. There's also a possibility. We can go back in history and publish resolved schema
for semcom older versions. So we can get rid of version one support and point at the resolve schema as a workaround.
That's another thing that I've been thinking about like depending on how how this goes. But if you want to know why, I'm really targeting like the front end piece. It's because I want to get the repo up to date as quickly as possible. So our build horizon for weaver and maintaining all of this, Gunk
goes away as quickly as possible. Right.
**Laurent Quérel** 42:22 Hmm.
**Josh Suereth** 42:23 So
anyway, this is this is what the prototype looks like. If you have concerns, let me know. But that's why I want to do a bunch of cleanup.
I I can probably do that in a separate Pr, so it's easier to see, and then it'll make a lot of sense when you see this, because this is how we're doing the
I'm sorry.
All right.
This is how we're doing the version and version suggestions. Last week Ludmilla and Jeremy recommended that we have. We.
**Laurent Quérel** 43:01 What did you say?
My connection issue.
**Jeremy Blythe** 43:07 I think he just broke.
**Josh Suereth** 43:14 Hey? I'm back.
**Laurent Quérel** 43:15 We did.
**Josh Suereth** 43:16 About that. There's 2 of me apparently.
**Laurent Quérel** 43:21 Yeah.
**Jeremy Blythe** 43:22 Pretty weird. You sneezed, and then you went offline.
**Laurent Quérel** 43:25 It was super fool that you killed your connection.
**Josh Suereth** 43:28 I didn't know. I didn't know I could infect my computer with a virus, you know.
No, so anyway, this this was the thing that Ludmilla and Jeremy recommended last week. So this is the result of me prototyping that and getting that to work. I think I think this will work.
I think we get decent enough error messages. The only problem I have is if you don't put version in
the error message around. Unversion is still weird, Wonky as hell a little bit
that I'm not super happy about it. But it's okay.
**Laurent Quérel** 44:00 Yeah. The only option for that would be to to integrate what I did. That is still not because that will be an in where everything will be well,
I think that's that's why started to to go in this direction. But it was way too much work to deliver that before my the other stuff before my Pt.
**Josh Suereth** 44:24 Right.
I understand how much work it is. That's why I just I. But the but the thing is that work is only helping error messages where I think the fundamental problem is the Yaml itself. If you read, if you read these Yaml examples right? It's just, it's so much nicer.
**Laurent Quérel** 44:42 No, yes, I agree. I mean, I'm super happy with this new approach.
When we talk about, use ease of use or user experience.
This one is is massive.
**Josh Suereth** 44:54 Yeah, okay, I'll continue working on that. That's basically occupying all of my weaver time.
Yeah, as you know, having tried to do it. Yeah. So multi register support for more than 2 levels. Let's talk about that, Lauren. Take it away.
**Laurent Quérel** 45:13 Yeah. So that's something that Jeremy needs for some some future initiative he has in its own company. And obviously it's something that I also have basically the same kind of requirement. Basically, it's the option to have a registry at a corporate level and registry at a project level. For example.
so that means that we need now 3 level and maybe more for more complex companies. Where you have a corporate level, you have a business unit level and blah blah, so basically supporting more than one level, it's still flat. There, we we don't want to enter into a situation where we have, obviously, security dependencies, and we don't want to enter into a situation where we resolve a dag. We still resolve a very flat hierarchy.
I think it's super easy to achieve. I don't see any problem. Personally, I think the existing code is
mostly already there to support that we just have to making sure that we, we enforce these 2.
2. Validation. 1st is low circular dependency. I think it's already there, second, making sure that it's a flat organization, and there is no complex dag.
If that's the case, then we authorize as much as level that you want and then as and that map to a a company organization.
As a as a project maintainer you. You define your custom registry which imports the the Enterprise level registry which imports, the the Semantic convention registry, and then same thing for other projects. But they are independent hierarchies. I think that will work nicely, and we cover
a lot of situation before entering into the most complex approach from tier g. 3. That is described into the document. But we require a lot of work regarding the resolution
because we could have a collision, we could have other things like that. So then.
I think that's what I'd like to
to to achieve like an intermediary step before, to enter to the full material registry support.
Generally it's it's reflecting well what you expect also on your side.
**Jeremy Blythe** 47:50 Yeah. So what I imagine happening is that
as as someone making a small application somewhere, some micro service, or
in a lot of my cases coming up. These are like hardware devices
running like really small cpus, with like some very tuned like C code on there, or whatever
I don't want. They don't want to have import some giant code generation of like all of everything. So this is where we come to like the the work that we did on like importing, referencing. Just what I need from for this application over here. But it's coming from some enterprise level thing.
and the enterprise level thing is making reference to open telemetry.
Sem conf.
I'm just wondering whether there may be situations where this thing, the this small device, with its own
model, may also need to reference the open timetry independently, so that it could.
**Laurent Quérel** 49:02 Oh, that will become yeah.
**Jeremy Blythe** 49:06 Would that be too difficult if it has to be a chain? That's still okay.
**Laurent Quérel** 49:09 That will that will become more problematic, because if we have this small custom registry for for the application, the final application?
Then we could end up into a situation where, at the corporate level, you import version one dot 32 for authentication, and the application. Import 1 34,
and then we enter into the situation that is described into the
the result of the the multi registry support document.
It's feasible, but it's something that will be much more work than what I was suggesting.
**Jeremy Blythe** 49:46 That's fine, and I'm happy. With that I was just. We can have that restriction, and that's fine.
**Laurent Quérel** 49:51 Yeah, so.
**Jeremy Blythe** 49:52 In a way, it's quite nice, because it it forces the application writer down at this end
to put it into the, and they have to put it into the corporate or the enterprise registry.
But all they're doing is they're just pulling in what they need specifically for this. So it all goes in the central place.
**Laurent Quérel** 50:10 Yeah.
So let let me reformulate the the approach to make sure that it that could
match your needs. At the corporate level, we could say.
you can define corporate level signals or attributes.
But in the import section you import everything from open telemetry and at the application level.
What you do is you define your own specific signal, if you need, and you import the specific on the 2 others
so you end up with at the application level. You end up with something relatively small and just focus on the application need. And and at the corporate level. The convention will be okay. You import everything from 17 convention, so they will be visible. So we are not entering into the situation that you described. We need a second import to the 70 convention, because it's already included, included, I think, as an intermediary solution, I think that will work.
**Jeremy Blythe** 51:22 Okay, yeah, I really look at. Because what I've been experimenting with once.
once you've once you've kind of
shrunk it down through to just what your application needs.
then your code generation can be very specific.
**Laurent Quérel** 51:38 Yeah.
**Jeremy Blythe** 51:39 Just down at this end for just the things you need. You can almost like.
That's why I was just.
I was able to go I was able to give to Claude like, oh, well, I want my metrics to like. I need the code to look like this.
The gamble, and I gave it that example, and it just went.
**Laurent Quérel** 51:57 We want also to achieve on on a different project. For example, for the hotel project, the the rest base, the telephone which I'm working. We we at some point, we want to use convention. And and we were
to generate optimized
client SDK, that are type safe and just with the the what we need, and nothing else. No, no abstraction, no, nothing. A direct a direct reporting of those metrics, or whatever we we want to report as fast as possible. So it's more than just type safe. It's also optimized.
**Jeremy Blythe** 52:39 Exactly.
**Laurent Quérel** 52:39 Thank you.
**Jeremy Blythe** 52:41 Yeah.
**Laurent Quérel** 52:42 Yeah, to tell you. And in your context of a small device with a small resources that totally makes sense to have something that will be
minimal.
**Jeremy Blythe** 52:54 Yeah, exactly like, you know, I was talking to them one of the reasons they hadn't moved forwards
yet. They're one of this. One of these teams is that they were like they looked at the SDK, and they're like, Oh, I can't! I can't exist again. I'm like, well, you could just you can use the proto right and just
go direct. You don't need to pull in this whole SDK,
so their code generation would be something that is like directly related to the way that they're going to like use the you know, whatever they've generated for the.
**Laurent Quérel** 53:24 Yeah, yeah.
**Jeremy Blythe** 53:24 See what I mean. So it's going to be completely different necessarily from something else. We may. We may generalize in weaver that would likely be related directly to using the St. Various sdks. Right? So it's
that's why it's really nice that this flow, anyway, I think it's gonna be really good. I'm talking to my team tomorrow.
load a bunch of other teams that do hardware. So I didn't do hardware stuff. So
I'm going to get some more feedback after tomorrow, as well.
**Laurent Quérel** 53:55 Yeah, I'm not sure when I will be able to work on that.
But I think I have a pretty good idea on what need to be done.
I don't think we are so far from being being able to support that
The only thing is to see the interaction between what we had initially to support 2 level and what we recently had for the import in the import section. I like to to check what that mean when we have more than one import section, because the the in Hotel river we don't have that. And then, but in the custom registry at the company level in the Custom Registry at the application level. Then we have 2 import section.
I don't see why that will not work, but maybe they are something that I missed. That are hidden into the code that will make that complicated.
But that that's the only unknown right now I have in mind.
Really, would you agree with them
with this intermediary step for meteor registry support you? Are, you are mute.
**Josh Suereth** 55:14 Interesting. I clicked on mute. All right, anyway. Yes. One thing I was thinking about, though.
You could. You could allow dependencies if they're exactly the same version.
**Laurent Quérel** 55:27 Yeah, that could be also another. Yeah. But.
**Josh Suereth** 55:31 Option. I don't want to make this more complicated. So whatever you think is reasonable to do relatively quickly, I think we need to evolve
and I kind of don't want to make a complete dependency management solution in the long run, because I did that when I owned a build tool, and it's.
**Laurent Quérel** 55:46 I remember your comment on that personally. Even if we could do what you said.
I think that could be a nightmare as a user, because the the enterprise level custom registry
will be slightly independent, I mean will be independent in terms of management with all the application level custom registry which are dependent on this one.
and then they could decide to change their version. But that will not be changed in one of the application customer history
which will make all the the build failing. And I think it's it's problematic. So
what I discovered, I think, does not
simplify that because the only person responsible to define the the open telemetry registry version will be at the corporate level.
And they can't. They can't introduce issues
by by mistake, I think, with this approach.
**Josh Suereth** 56:57 That's fair. That's fair. Okay, yeah, I. Yeah, I.
The other thing, like, I hear what you're saying. But I also think, it's the same problem, because
if the application has a different version of hotel semcom than the corporate version, their build breaks. But when they update the corporate version, they'd have to update their version of semcom at the same time to not have their build break.
So they what? So if the corporate version depends on some they would always have to upgrade in lockstep, which is what you're implicitly doing. It's just like, anyway, I don't want to belabor the point. It's a thing to consider if we think it would provide value.
But what you propose, I think, is totally fine, like it. It solves the use case. It gets us moving.
And again I want. I want us to make progress here.
so I don't think it locks any doors that we would be sad if they're locked.
is the other thing.
**Laurent Quérel** 57:55 Yeah.
**Jeremy Blythe** 57:57 So. And it's a really good pattern. And I think it shows for large
corporations that want to do this kind of application level, like specific model driven.
you know, observing, it's it's the observability by design thing. It unlocks that for
not just toy applications. Right? This is it, for, like large corporation stuff like it's the 1st step really in that. In that mode.
**Josh Suereth** 58:24 Yeah.
I have to drop. But consider this. Consider extensions to semcom. So imagine opentelemetry semcom as the base imagine. There is a azure semcon based on opentelemetry. Imagine there's a Gcp. Based on opentelemetry. And now I'm a corporation, and I want to use the Gcp one, and I want to use the azure.
**Laurent Quérel** 58:44 Oh, yes, that's.
**Josh Suereth** 58:45 Yeah, that. So so that's still blocked as a use case. But like.
that's probably fine for now, because we don't have that yet. So let's get yeah, alright. I gotta jump. Thanks. Everybody.
**Laurent Quérel** 58:58 But.
**Jeremy Blythe** 58:59 Cheers.
